import os
from openai import OpenAI
from typing import AsyncGenerator

# set openai api key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


async def generate_description(input) -> AsyncGenerator[str, None]:
    messages = [
        {"role": "system",
         "content": """ As a product Description Generator,Generate  very short concise rich text product description with emojis from the information provided to you"""}
    ]

    messages.append({"role": "user", "content": f"{input}"})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            yield content

    # reply = completion.choices[0].message.content
    # return reply
