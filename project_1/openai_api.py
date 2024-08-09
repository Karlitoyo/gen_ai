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

system_role_content = "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
MODEL="gpt-3.5-turbo"

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": system_role_content},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ],
  temperature=0.7,
)

print("Response:",completion.choices[0].message.content)
print("Usage:",completion.usage)
print("Model:",completion.model)