import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import display, Image
import base64
image_path = "../images/triangle.png"
display(Image(image_path))

load_dotenv()

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("The OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        image_binary = img_file.read()
        return base64.b64encode(image_binary).decode("utf-8")

base64_image = image_to_base64(image_path)

MODEL="gpt-4o"

system_message = "You are a computer vision model that can identify shapes in images."
prompt = f"Identify the shape in the image below and provide a brief description of its properties."
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": [
        {"type": "text", "text": prompt},
        {"type": "image_url", 'image_url': {
            'url': f"data:image/png;base64,{base64_image}"},
        },]}
    ],
    temperature=0
)


print("Response:",response.choices[0].message.content)
print("Usage:",response.usage)
print("Model:",response.model)