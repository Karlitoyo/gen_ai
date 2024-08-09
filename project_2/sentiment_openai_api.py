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
MODEL="gpt-3.5-turbo"
emotions = ["joy", "sadness", "anger", "fear", "surprise", "disgust"]
prompt = f'''AI will take over the world!'''

def getSentiment(prompt, emotions):
    system_prompt = f'''You are an emotionally intelligent assistant.
    Classify the sentiment of user's text with ONLY ONE OF THE FOLLOWING EMOTIONS: {emotions}.
    After classifying the text, respond with the emotion ONLY.'''
    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens = 20,
        temperature = 0.0
    )
    r = response.choices[0].message.content
    if r == '':
        r = "I'm sorry, I couldn't classify the sentiment."
    return r

print("Response:", getSentiment(prompt, emotions))