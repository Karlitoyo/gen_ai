import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("The OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)

MODEL="gpt-4o"

system_message = "You respond in English and then translate your response into Japanese."
prompt = "Write a short and concise description of this image."
image_url = "https://upload.wikimedia.org/wikipedia/commons/9/98/Aldrin_Apollo_11_original.jpg"

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": [
        {"type": "text", "text": prompt},
        {"type": "image_url", 'image_url': {
            'url': image_url},
        },]}
    ],
    temperature=0
)


print("Response:",response.choices[0].message.content)
print("Usage:",response.usage)
print("Model:",response.model)