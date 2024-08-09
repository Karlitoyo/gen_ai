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
prompt = "a photorealistic image of Shenron from dragonball z in a vivid style and black background with the dragon balls in the background numbered from 1 to 7 with small black stars scattered around the image"

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  style="vivid",
  size="1024x1024",
  quality="standard",
  n=1
)

image_url = response.data[0].url
print("Image URL:", image_url)