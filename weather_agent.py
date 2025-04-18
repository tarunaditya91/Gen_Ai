# from dotenv import load_dotenv
# from openai import OpenAI
# import requests
# import json
# load_dotenv()


# client = OpenAI()

# def get_weather(city: str):
#     print("tool called: get_weather",city)
#     url = f"https://wttr.in/{city}?format=%C+%t"
#     responce = requests.get(url)

#     if responce.status_code == 200:
#         return f"the weather in {city} is {responce.text}."
#     return "something is wrong"


# available_tools ={
#     "get_weather":{
#         "fn":get_weather,
#         "description":"takes the city input and give the temperature"
#     }
# }




# system_prompt ="""
# you are an helpful ai assistant who is specialized in resolving user query.
# you work on start , plan, action, observe mode.
# for the given user query and available tools , plan the steps by step exection , based on the planning,
# select the relavent tool from the available tool. and based on the tool selection you  perform an action to call the tool
# wait for the observation and based on the observation from the tool call reserve the user query.

# Rules:
# 1.Follow the strict JSON  output as per output schema.
# 2.Always perfome one step at a time
# 3 carefully analyse the user query

# Output JSON Format:
# {{
#     "step":"string",
#     "content":"string",
#     "function":"the name of function if the step is action",
#     "input":"the inputn parameter of the function",
# }}

# Available tools:
# get_weather: takes the city input and give the temperature


# Example :
# User Query what is the weather of new york?
# output: {{"step":"plan","content":"the user is intrested in weather data of new york"}}
# output: {{"step":"plan","content":"from the available tool i should call get_weather"}}
# output: {{"step":"action","function":"get_weather","input":"new york"}}
# output: {{"step":"observe","output:"12 degree cel"}}
# output: {{"step":"output","content":"the weather of new york in  to be 12 degrees."}}
# """

# messages =[
#     {"role":"system","content":system_prompt}
# ]

# user_query = input("enter you question")
# messages.append({"role":"user","content": user_query})

# while True:
#     result = client.chat.completions.create(
#     model = "gpt-4o",
#     messages = messages
#     )
#     parsed_output = json.loads(result.choices[0].message.content)
#     messages.append({"role":"assistent","content":json.dumps(parsed_output)})

#     if parsed_output.get("step") == "plan":
#         print(f"brain:  {parsed_output.get("content")}")
#         continue
#     if parsed_output.get("step") == "action":
#         tool_name = parsed_output.get("function")
#         tool_input = parsed_output.get("input")

#         if available_tools.get(tool_name,False) !=False:
#             output = available_tools[tool_name].get("fn")(tool_input)
#             messages.append({"role":"assistant","content":json.dumps({"step":"observe","output":output})})
#             continue
#     if parsed_output.get("step") == "output":
#         print(f"boat : {parsed_output.get("content")}")
#         break

from dotenv import load_dotenv
from openai import OpenAI
import requests
import json
import os

# Load environment variables (like OPENAI_API_KEY)
load_dotenv()

# Initialize OpenAI client
client = OpenAI()
def run_command(command):
    result = os.system(command=command)
    return result

# print(run_command("ls"))
# Tool definition
def get_weather(city: str):
    print("Tool called: get_weather", city)
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."
    return "Something went wrong."

# Available tools dictionary
available_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Takes the city input and gives the temperature"
    },
    "run_command":{
        "fn":run_command,
        "description":"take the command and execute on the system and return the output"
    }
}

# System prompt
system_prompt = """
You are a helpful AI assistant who is specialized in resolving user queries.
You work in the following steps: plan, action, observe, output.
For a given user query and available tools, plan the step-by-step execution.
Based on planning, select the relevant tool from the available tools and call the tool.
Wait for the observation, then resolve the user query.

Rules:
1. Follow the strict JSON output as per the output schema.
2. Always perform one step at a time.
3. Carefully analyze the user query.

Output JSON Format:
{{
    "step": "string",
    "content": "string",
    "function": "name of function if step is action",
    "input": "input parameter for the function"
}}

Available tools:
get_weather: Takes the city input and gives the temperature.
run_command: take the command and execute on the system and return the output

Example:
User Query: What is the weather of New York?
output: {{"step": "plan", "content": "The user is interested in the weather data of New York."}}
output: {{"step": "plan", "content": "From the available tool, I should call get_weather."}}
output: {{"step": "action", "function": "get_weather", "input": "New York"}}
output: {{"step": "observe", "output": "12 degree Celsius"}}
output: {{"step": "output", "content": "The weather of New York is 12 degrees Celsius."}}
"""

# Start chat history
messages = [
    {"role": "system", "content": system_prompt}
]

# Get user query
user_query = input("Enter your question: ")
messages.append({"role": "user", "content": user_query})

# Main loop
while True:
    result = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    parsed_output = json.loads(result.choices[0].message.content)
    messages.append({"role": "assistant", "content": json.dumps(parsed_output)})

    step = parsed_output.get("step")

    if step == "plan":
        print(f"🧠 Brain: {parsed_output.get('content')}")
        continue

    if step == "action":
        tool_name = parsed_output.get("function")
        tool_input = parsed_output.get("input")

        if tool_name in available_tools:
            output = available_tools[tool_name]["fn"](tool_input)
            messages.append({
                "role": "assistant",
                "content": json.dumps({"step": "observe", "output": output})
            })
            continue

    if step == "output":
        print(f"🤖 Bot: {parsed_output.get('content')}")
        break







