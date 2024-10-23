from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv(".env")

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

file_path = "/Users/juanreyesgarcia/Dev/Python/LLMSandbox/data/llama2.pdf"


def load_and_split(file_path: str) -> list:
    loader = PyPDFLoader(file_path)

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(docs)

def in_memory_openai_lc_rag(file_path: str) -> str:
    llm = ChatOpenAI(model="gpt-4o", temperature=0.1, max_tokens=1024, api_key=OPENAI_API_KEY)

    splits = load_and_split(file_path)


    vectorstore = InMemoryVectorStore.from_documents(
        documents=splits, embedding=OpenAIEmbeddings()
    )

    retriever = vectorstore.as_retriever()

    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )


    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    results = rag_chain.invoke({"input": "In 10 words explain the paper"})

    return results["answer"]

def chroma_anthropic_lc_rag(file_path: str) -> str:
    
    llm = ChatAnthropic(model="gpt-4o", temperature=0.1, max_tokens=1024, api_key=ANTHROPIC_API_KEY)

