import openai

import os
from openai import OpenAI

key = "Your API KEY"

client = OpenAI(
    # This is the default and can be omitted
    api_key=key
)
messages = []

def completion(message):
    global messages

    messages.append(
        {
            "role" : "user",
            "content" : message
        }
    )

    chat_completion = client.chat.completions.create( messages = messages,
                model="gpt-4o"
    )
    message = {
        "role" : "assistant",
        "content" : chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis : {message['content']}")

if __name__ == "__main__":
    print(f"Jarvis : Hello I am Jarvis, How may i help you\n")
    while True:
        user_question = input()
        print(f"User : {user_question}")
        completion(user_question)