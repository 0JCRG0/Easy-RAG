
import re
from chromadb.utils import embedding_functions
import tiktoken
import psycopg2
import pandas as pd
import logging
import timeit
import json
from datetime import datetime, timedelta
from torch import Tensor
from transformers import AutoTokenizer, AutoModel
import pyarrow.parquet as pq
from aiohttp import ClientSession
from pgvector.psycopg2 import register_vector
from dotenv import load_dotenv
import os

# Configure the logger with the custom format
log_format = '%(asctime)s %(levelname)s: \n%(message)s\n'

logging.basicConfig(filename="/Users/juanreyesgarcia/Dev/Python/RAG/logging.log",
	level=logging.INFO,
	format=log_format)

load_dotenv(".env")
LOCAL_POSTGRE_URL = os.environ.get("LOCAL_POSTGRE_URL")



def clean_rows(s):
	if not isinstance(s, str):
		print(f"{s} is not a string! Returning unmodified")
		return s
	s = re.sub(r'\(', '', s)
	s = re.sub(r'\)', '', s)
	s = re.sub(r"'", '', s)
	s = re.sub(r",", '', s)
	return s

def openai_ef(OPENAI_API_KEY):
	openai_embedding = embedding_functions.OpenAIEmbeddingFunction(
					api_key=OPENAI_API_KEY,
					model_name="text-embedding-ada-002"
				)
	return openai_embedding

def truncated_string(
	string: str,
	model: str,
	max_tokens: int,
	print_warning: bool = False,
) -> str:
	"""Truncate a string to a maximum number of tokens."""
	encoding = tiktoken.encoding_for_model(model)
	encoded_string = encoding.encode(string)
	truncated_string = encoding.decode(encoded_string[:max_tokens])
	if print_warning and len(encoded_string) > max_tokens:
		print(f"Warning: Truncated string from {len(encoded_string)} tokens to {max_tokens} tokens.")
	return truncated_string

def num_tokens(text: str, model: str ="gpt-3.5-turbo") -> int:
	#Return the number of tokens in a string.
	encoding = tiktoken.encoding_for_model(model)
	return len(encoding.encode(text))



def count_words(text: str) -> int:
	# Remove leading and trailing whitespaces
	text = text.strip()

	# Split the text into words using whitespace as a delimiter
	words = text.split()

	# Return the count of words
	return len(words)



def average_pool(last_hidden_states: Tensor,
				attention_mask: Tensor) -> Tensor:
	last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
	return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

def e5_base_v2_query(query):
	tokenizer = AutoTokenizer.from_pretrained('intfloat/e5-base-v2')
	model = AutoModel.from_pretrained('intfloat/e5-base-v2')

	query_e5_format = f"query: {query}"

	batch_dict = tokenizer(query_e5_format, max_length=512, padding=True, truncation=True, return_tensors='pt')

	outputs = model(**batch_dict)
	query_embedding = average_pool(outputs.last_hidden_state, batch_dict['attention_mask']).detach().numpy().flatten()
	return query_embedding

def filter_last_two_weeks(df:pd.DataFrame) -> pd.DataFrame:
	# Get the current date
	current_date = datetime.now().date()
	
	# Calculate the date two weeks ago from the current date
	two_weeks_ago = current_date - timedelta(days=14)
	
	# Filter the DataFrame to keep only rows with timestamps in the last two weeks
	filtered_df = df[df["timestamp"].dt.date >= two_weeks_ago]
	
	return filtered_df

def passage_e5_format(raw_descriptions:list) -> list:
	formatted_batches = ["passage: {}".format(raw_description) for raw_description in raw_descriptions]
	return formatted_batches

def query_e5_format(raw_descriptions:list) -> list:
	formatted_batches = ["query: {}".format(raw_description) for raw_description in raw_descriptions]
	return formatted_batches

def set_dataframe_display_options():
	# Call the function to set the desired display options
	pd.set_option('display.max_columns', None)  # Show all columns
	pd.set_option('display.max_rows', None)  # Show all rows
	pd.set_option('display.width', None)  # Disable column width restriction
	pd.set_option('display.expand_frame_repr', False)  # Disable wrapping to multiple lines
	pd.set_option('display.max_colwidth', None)  # Display full contents of each column


def to_postgre(df: pd.DataFrame):

	table = "fast_rag"
	db_url = LOCAL_POSTGRE_URL

	try:
		# create a connection to the PostgreSQL database
		cnx = psycopg2.connect(db_url)

		logging.info(f" Sending jobs to local test db")

		# create a cursor object
		cursor = cnx.cursor()
		cursor.execute('CREATE EXTENSION IF NOT EXISTS vector')

		#Register the vector type with your connection or cursor
		register_vector(cnx)

		create_table_if_not_exist = f""" 
			CREATE TABLE IF NOT EXISTS {table} (
			id SERIAL PRIMARY KEY,
			chunks TEXT,
			embeddings vector(1024)
			);"""
		
		cursor.execute(create_table_if_not_exist)

		# execute the initial count query and retrieve the result
		initial_count_query = f"""
			SELECT COUNT(*) FROM {table}
		"""

		cursor.execute(initial_count_query)
		initial_count_result = cursor.fetchone()
		
		""" IF THERE IS A DUPLICATE ID IT SKIPS THAT ROW & DOES NOT INSERTS IT
			IDs UNIQUENESS SHOULD BE ENSURED DUE TO ABOVE.
		"""
		jobs_added = []
		for index, row in df.iterrows():
			insert_query = f"""
				INSERT INTO {table} (chunks, embeddings)
				VALUES (%s, %s)
				RETURNING *
			"""
			values = (row['chunks'], row['embeddings'])
			cursor.execute(insert_query, values)
			affected_rows = cursor.rowcount
			if affected_rows > 0:
				jobs_added.append(cursor.fetchone())


		""" LOGGING/PRINTING RESULTS"""

		final_count_query = f"""
			SELECT COUNT(*) FROM {table}
		"""
		# execute the count query and retrieve the result
		cursor.execute(final_count_query)
		final_count_result = cursor.fetchone()

		# calculate the number of unique jobs that were added
		if initial_count_result is not None:
			initial_count = initial_count_result[0]
		else:
			initial_count = 0
		jobs_added_count = len(jobs_added)
		if final_count_result is not None:
			final_count = final_count_result[0]
		else:
			final_count = 0

		# check if the result set is not empty
		print("\n")
		print(f"{table} Table Report on test:", "\n")
		print(f"Total count of jobs before crawling: {initial_count}")
		print(f"Total number of unique jobs: {jobs_added_count}")
		print(f"Current total count of jobs in PostgreSQL: {final_count}")

		postgre_report = f"{table} Table Report on test:"\
						"\n"\
						f"Total count of jobs before crawling: {initial_count}" \
						"\n"\
						f"Total number of unique jobs: {jobs_added_count}" \
						"\n"\
						f"Current total count of jobs in PostgreSQL: {final_count}"

		logging.info(postgre_report)

		# commit the changes to the database
		cnx.commit()

		# close the cursor and connection
		cursor.close()
		cnx.close()
	except Exception as e:
		logging.error(f"Exception at to_embeddings_e5_base_v2().\nException as follows: {e}.\n")
		raise Exception