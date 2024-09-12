from mistralai.async_client import MistralAsyncClient
import chainlit as cl
from dotenv import load_dotenv
import os

load_dotenv()

mai_client = MistralAsyncClient(api_key=os.environ.get("MISTRAL_API_KEY"))

# Instrument the Mistral AI client
cl.instrument_mistralai()

settings = {
    "model": "mistral-large-latest",
    "temperature": 0,
}

@cl.on_message
async def on_message(message: cl.Message):
    response = await mai_client.chat(
        messages=[
            {
                "content": "You are a helpful bot, you always reply in Spanish",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()
