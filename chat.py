from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api = os.getenv("GEN_API_KEY")
client = genai.Client(api_key = gemini_api)


response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is the sky blue?'
)
print(response.text)
# this type of prompting is known as zeroshot prompting


