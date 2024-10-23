import ell
from sklearn.metrics.pairwise import cosine_similarity
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np

load_dotenv()

ell.init("./logdir", verbose=True)

system_prompt = """ You are a helpful assistant. Only use the most relevant information to solve the user query. If you do not know the answer say 'I do not know' The relevant chunks are enclosed in <chunks> tags and query in query <query> tags"""

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

MODELS = ["claude-3-5-sonnet-20240620", "gpt-4o"]


data = ["Artificial intelligence is transforming the medical field with new diagnostic and treatment options.", "Machine learning is increasingly used for analyzing large data sets in finance.", "Recent advancements in natural language processing include better context understanding."]


def embed_chunks() -> list:

    embeddings_model = OpenAIEmbeddings()
    embeddings = embeddings_model.embed_documents(data
        
        )

    return embeddings 

chunk_embeddings = embed_chunks()

data_dict = {"chunks": data, "embeddings": chunk_embeddings}

df = pd.DataFrame(
    data_dict
)



def embed_query(query: str) -> list:

    embeddings_model = OpenAIEmbeddings()
    embeddings = embeddings_model.embed_documents([query]
        )

    return embeddings 


@ell.complex(model="gpt-4o", max_tokens=1200)
def simple_rag(chunk: str, query: str, system_prompt: str = system_prompt):
    return [
        ell.system(system_prompt),
        ell.user(f"<query>{query}</query> <chunk>{chunk}</chunk> ")
    ]

if __name__ == "__main__":
    questions = ["How is AI transforming the medical field?", "How is machine learning used in finance?", "What are recent advancements in natural language processing?"]
    query = questions[0]
    embeded_query = embed_query(query)

    embeded_chunks = embed_chunks()
    relevance_score = cosine_similarity(embeded_query, list(df["embeddings"]))    
    
    idx = np.argmax(relevance_score)

    relevant_chunk = data[int(idx)]

    print(relevant_chunk)

    simple_rag(chunk=relevant_chunk, query=query)
    