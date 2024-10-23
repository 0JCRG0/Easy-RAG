from dotenv import load_dotenv
import os
from ell.lmp.complex import complex
from ell.types.message import system, user
import ell
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

MODELS = ["claude-3-5-sonnet-20240620", "gpt-4o"]

ell.init(store="./logdir", autocommit=True, verbose=True)
file_path = "/Users/juanreyesgarcia/Dev/Python/LLMSandbox/data/llama2.pdf"

system_prompt = """
    You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer
    the question. If you don't know the answer, say that you
    don't know. Use three sentences maximum and keep the
    answer concise."""

def load_split_embed_and_find_top_n(query: str, file_path: str = file_path, n: int = 5) -> list:
    loader = PyPDFLoader(file_path)

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    
    splits = text_splitter.split_documents(docs)

    vectorstore = InMemoryVectorStore.from_documents(
        documents=splits, embedding=OpenAIEmbeddings()
    )

    return vectorstore.similarity_search(query, k=n)


@complex(
model="gpt-4o",
temperature=0.1,
max_tokens=4096)
def rag(query: str, chunks: list, system_prompt: str = system_prompt):
    return [
        system(system_prompt),
        user(f"<query> {query} </query> <chunks> {chunks} </chunks>"),
    ]


if __name__ == "__main__":
    query="what is the architecture of LLAMA2?"
    chunks = load_split_embed_and_find_top_n(query=query)
    ans = rag(query=query, chunks=chunks)



