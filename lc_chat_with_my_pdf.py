from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv(".env")

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

file_path = "/Users/juanreyesgarcia/Dev/Python/LLMSandbox/data/llama2.pdf"

loader = PyPDFLoader(file_path)

llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

docs = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)


vectorstore = InMemoryVectorStore.from_documents(
    documents=splits, embedding=OpenAIEmbeddings()
)

retriever = vectorstore.as_retriever()

