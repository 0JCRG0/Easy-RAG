import numpy as np
import pandas as pd
import logging
from pgvector.psycopg2 import register_vector
import psycopg2
from openai import OpenAI
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, retry_if_exception_type, before_sleep_log, stop_after_attempt
import os
import voyageai
import tiktoken
import anthropic
from utils.prompts import *


log_format = '%(asctime)s %(levelname)s: \n%(message)s\n'

logging.basicConfig(filename="/Users/juanreyesgarcia/Dev/Python/RAG/logging.log",
	level=logging.INFO,
	format=log_format)

load_dotenv(".env")

LOCAL_POSTGRE_URL = os.environ.get("LOCAL_POSTGRE_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
VOYAGE_API_KEY = os.environ.get("VOYAGE_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

vo = voyageai.Client(api_key=VOYAGE_API_KEY)

def individual_voyage_query_embedding(query):
	result = vo.embed(query, model="voyage-2", input_type="query", truncation=True)
	embedding = np.array(result.embeddings)
	return embedding

def multiple_voyage_query_embedding(query):
	result = vo.embed(query, model="voyage-2", input_type="query", truncation=True)
	embedding = np.array(result.embeddings)
	return embedding

def num_tokens(text: str, model: str ="gpt-3.5-turbo-1106") -> int:
	#Return the number of tokens in a string.
	encoding = tiktoken.encoding_for_model(model)
	return len(encoding.encode(text))

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

@retry(stop=stop_after_attempt(7), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(Exception), before_sleep=before_sleep_log(logger, logging.WARNING))
def Answer(
	query: str,
	formatted_extracts: str,
	system_prompt: str,
	provider: str = "Anthropic",
	model: str = "claude-3-opus-20240229",
) -> pd.DataFrame:
	"""
	An AI assistant that answers a user's query with the assistance of the most similar answers
	"""
	
	if provider == "OpenAI":
		logging.info(f"""CALLING: {model} """)

		client = OpenAI(
			api_key=OPENAI_API_KEY,
		)

		response = client.chat.completions.create(
			messages = [
				{"role": "system", "content": system_prompt},
				{"role": "user", "content": f"****{query}****\n####{formatted_extracts}####"}
			],
			
			model=model,
			temperature=0,
		)
		
		response_message = response.choices[0].message.content

		logging.info(f"gpt_4_response:\n\n{response_message}")
	
	elif provider == "Anthropic":
		client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
		response = client.messages.create(
						model=model,
						system=system_prompt,
						temperature=0,
						max_tokens=2000,
						messages=[
							{"role": "user", "content": f"****{query}****\n####{formatted_extracts}####"}
						]
					)
		response_message = response.content[0].text

	return response_message

@retry(stop=stop_after_attempt(7), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(Exception), before_sleep=before_sleep_log(logger, logging.WARNING))
def MultipleAnswers(query:str, raw_doc: str, sys_prompt: str = multiple_answers_prompt_base, provider: str= "Anthropic", model: str = "claude-3-haiku-20240307") -> str:
	
	logging.info(f"""CALLING: {model} """)
	

	if provider == "OpenAI":

		client = OpenAI(
			api_key=OPENAI_API_KEY,
		)

		response = client.chat.completions.create(
			messages = [
				{"role": "system", "content": sys_prompt},
				{"role": "user", "content": f"****{query}****\n####{raw_doc}####"}
			],
			
			model="gpt-4-1106-preview",
			temperature=0,
		)
		
		response_message = response.choices[0].message.content
	
	elif provider == "Anthropic":
		client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
		response = client.messages.create(
						model=model,
						system=sys_prompt,
						temperature=0,
						max_tokens=2000,
						messages=[
							{"role": "user", "content": f"****{query}****\n####{raw_doc}####"}
						]
					)
		response_message = response.content[0].text

	logging.info(f"MultipleAnswers() response:\n\n{response_message}")

	return response_message

#Make connection and enable pgvector
conn = psycopg2.connect(LOCAL_POSTGRE_URL)
cursor = conn.cursor()
cursor.execute('CREATE EXTENSION IF NOT EXISTS vector')
register_vector(conn)

def filter_keywords(df: pd.DataFrame, parameters: list) -> pd.DataFrame:
	regex_pattern = r'\b(?:' + '|'.join(parameters) + r')\b'

	# Filter the DataFrame to only include rows with standalone words
	df_filtered = df[df['chunks'].str.contains(regex_pattern, case=False, regex=True, na=False)]

	return df_filtered


def FetchTopN(
		query_embedding: str,
		table_name: str,
		cursor=cursor,
		similarity_or_distance_metric: str = "NN",
	) -> pd.DataFrame:

	"""
	This function performs these actions:

	1. Filters user's country
	2. Performs similarity search depending on metric

	Returns a df containing the matching id and respective chunks
	"""
	
	metric_mapping = {
		"NN": "<->",
		"inner_product": "<#>",
		"cosine": "<=>"
	}

	# Check if the provided value exists in the dictionary
	if similarity_or_distance_metric in metric_mapping:
		similarity_metric = metric_mapping[similarity_or_distance_metric]
	else:
		logging.error("""Invalid similarity_or_distance_metric. Choose "NN", "inner_product" or "cosine" """)
		raise Exception("""Invalid similarity_or_distance_metric. Choose "NN", "inner_product" or "cosine" """)

	query = f"""
	SELECT id, chunks
	FROM {table_name}
	ORDER BY embeddings {similarity_metric} %s
	LIMIT 3;
	"""
	cursor.execute(query.format(table_name=table_name), query_embedding)

	# Fetch all the rows
	rows = cursor.fetchall()

	# Separate the columns into individual lists
	ids = [row[0] for row in rows]
	chunks = [row[1] for row in rows]

	df = pd.DataFrame({'id': ids, 'chunks': chunks})

	return df


def FormatTopN(df: pd.DataFrame) -> str:
    ids = df['id'].tolist()
    chunks = df["chunks"].to_list()
    token_budget = 128000
    
    message = "The following are the extracts with their respective IDs, only use this to answer the user's query:"
    for id, chunk in zip(ids, chunks):
        next_id = f'\n<Reference ID:{id}>\n---Extract: {chunk}---\n'
        if num_tokens(message + next_id, model="gpt-4") > token_budget:
            break
        else:
            message += next_id
    
    return message

def AnswerDoc(keywords: list | None, query: str) -> str:

	multiple_answers_output = MultipleAnswers(query=query, raw_doc=apricot_moose_md)

	answers = multiple_answers_output.split("====")

	answers = [s for s in answers if s.strip()]

	logging.info(f"answers:\n {answers}")

	accumulator = pd.DataFrame()
	for ans in answers:
		ans_embedding = multiple_voyage_query_embedding(ans)
		df_top_n = FetchTopN(ans_embedding, "apricot_moose")
		accumulator = pd.concat([accumulator, df_top_n], ignore_index=True)
		logging.info(f"accumulator before:\n {accumulator}")
	
	# Corrected the inplace operation and variable name
	accumulator.drop_duplicates(inplace=True)
	logging.info(accumulator)

	if keywords is not None:
		accumulator = filter_keywords(accumulator, keywords)
	
	formatted_message = FormatTopN(accumulator)
	logging.info(formatted_message)

	final_ans = Answer(query=query, formatted_extracts=formatted_message, system_prompt=answer_prompt_base)

	return final_ans

if __name__ == "__main__":
	keywords = None
	query = "What is the difference between opted in and opted out consent?"

	response = AnswerDoc(keywords, query)

	print(response)