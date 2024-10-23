from langchain_core.messages import HumanMessage
from langchain_anthropic import ChatAnthropic
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os

load_dotenv(".env")

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

model = ChatAnthropic(model="claude-3-5-sonnet-20240620")


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an extremely friendly chatbot. Engage in deep conversation.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

def call_model(state: MessagesState):
    chain = prompt | model
    response = chain.invoke(state)
    return {"messages": response}

workflow = StateGraph(state_schema=MessagesState)

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abd123"}}

def chat_bot(query: str):
    input_messages = [HumanMessage(query)]
    output = app.invoke({"messages": input_messages}, config)
    return output["messages"][-1].pretty_print() 

if __name__ == "__main__":
    while True:
        response = chat_bot(input("You: "))
