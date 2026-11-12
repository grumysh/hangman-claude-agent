from dotenv import load_dotenv
import anthropic
from anthropic import omit

from config import MAX_TOKENS, MODEL

load_dotenv()

client = anthropic.Anthropic()


def send(system, messages, tools=omit):
    return client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system,
        messages=messages,
        tools=tools,
    )


if __name__ == "__main__":
    response = send(
        system="You are a helpful assistant.",
        messages=[{"role": "user", "content": "Di hola en una frase corta."}],
    )

    for block in response.content:
        if block.type == "text":
            print(block.text)
