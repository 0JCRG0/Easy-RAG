import ell
from ell import Message
from dotenv import load_dotenv
import os

load_dotenv()


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

MODELS = ["claude-3-5-sonnet-20240620", "gpt-4o"]

ell.init(store="./logdir", autocommit=True, verbose=False)


@ell.complex(model="gpt-4o", temperature=0.7)
def chat_bot(message_history: list[Message]) -> list[Message]:
    return [
        ell.system("You are an extremely friendly chatbot. Engage in deep conversation."),
    ] + message_history

if __name__ == "__main__":
    message_history = []
    while True:
        user_input = input("You: ")
        message_history.append(ell.user(user_input))
        response = chat_bot(message_history)
        print("Bot:", response.text)
        message_history.append(response)