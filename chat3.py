from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()

client = OpenAI()

system_prompt ="""
you are an ai assistent who is expert inin breaking down the complex problems and then resolve the user query
for the given user input break down the problem step by step.
At least think 5-6 steps on how to solve the problem

these steps are you get input,you think,you again think several times before giving the answer

Example:
Input: what is 2+2.
output:{{step:"analyse,content:"useris intrested in maths}}
"""

result = client.chat.completions.create(
    model = "gpt-4",
    response_format={"type","json_object"},
    message=[
        {"role":"system","content": system_prompt}
        {"role":"user","content":"what is 3+4*5"}
        {"role":"assistent","content":}
    ]
)
print(result.choices[0].message.content)