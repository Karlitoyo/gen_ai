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
system_role="You are a helpful assistant."
text='''What are some interesting things to do in Istanbul?.'''
prompt = f'''Translate the following text into Japanese: "{text}"'''


def get_chat_completion(user_prompt, system_role=system_role, model=MODEL, temperature=1):
    
    messages = [
            {"role": "system", "content": system_role},
            {"role": "user", "content": user_prompt}
        ]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

response = get_chat_completion(prompt)
print("Response:",response)