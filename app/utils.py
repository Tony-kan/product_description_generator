import os
from openai import OpenAI

# set openai api key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def generate_description(input):
    messages = [
        {"role": "system",
         "content": """ As a product Description Generator,Generate short paragraph rich text product description with emojis from the information provided to you"""}
    ]

    messages.append({"role": "user", "content": f"{input}"})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = completion.choices[0].message.content
    return reply
