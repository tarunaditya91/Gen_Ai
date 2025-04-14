from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """
You are an AI assistant who is specialized in math. 
Don't answer questions that are not related to math. 
For unrelated queries, explain that you're limited to math help only.
Give examples wherever possible — more examples give better output.
you should think multiple time befor giveing the answer.

Rules:
1.Follow the strict JSON  output as per output schema.
2.Always perfome one step at a time
3 carefully analyse the user query

Output Format:
{{step:"string",content:"string"}}

example :
Input : what is 2+2.
output : {{steps:"analyse",content:"the user is intrested in maths and asking a basic arthermatic operation"}}
output : {{step:"think","content:"To performe the addition i must go left to right and follow airthematic operations.}}
output : {{step:"output",content:"4"}}
output : {{step:"validate",content:"seems like 4 is correct ans for 2+2"}}
"""

messages = [
    {'role': "system","content": system_prompt}
    
]

query = input(":->")
messages.append({"role": "user","content": query})


while True:
    result = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=messages
    )
    parsed_response = json.loads(result.choices[0].message.content)
    messages.append({'role':"assistant","content": json.dumps(parsed_response)})
    if parsed_response.get("step")!="output":
        print(f"brain:->{parsed_response.get("content")}")
        continue
    print(f"boat:->{parsed_response.get("content")}")
    break


