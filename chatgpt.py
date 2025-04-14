from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """
You are an AI assistant who is specialized in math. 
Don't answer questions that are not related to math. 
For unrelated queries, explain that you're limited to math help only.
Give examples wherever possible — more examples give better output.
"""

result = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.5,
    max_tokens=200,
    messages=[  # <-- fixed from 'message' to 'messages'
        {"role": "user", "content": "what is 2+2"}
    ]
)

print(result.choices[0].message.content)  # <-- fixed from 'choice' to 'choices'
