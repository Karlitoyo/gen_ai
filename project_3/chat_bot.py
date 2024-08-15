import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import openai
import time
load_dotenv()

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("The OPENAI_API_KEY environment variable is not set")

openai.api_key = api_key

questions = list()
bot_responces = list()
messages = list()

system_prompt = 'Answer as concisely as possible.'

messages.append({"role": "system", "content": system_prompt})

MODEL="gpt-3.5-turbo"

while True:
    current_question = input('Me:')
    if current_question.lower() in ['exit', 'quit']:
        print('Chat bot: I was happy to make your aquantance.')
        time.sleep(2)
        break
    if current_question == '':
        continue
    
    messages.append({"role": "system", "content": current_question})
    questions.append(current_question)
    
    response = openai.chat.completions.create(
    model = MODEL,
    messages=messages,
    temperature=0.7
)
    current_response = response.choices[0].message.content
    
    print(f'\nChat Bot: {current_response}')
    
    bot_responces.append(current_response)
    
    messages.append({"role": "assistant", "content": current_response})
    
    print('\n' + '-' *50  + '\n')
    
print()
print(dict(zip(questions, bot_responces)))
print('\n' + '-' *50  + '\n')

print()
print(messages)

# q1 = 'What are the healthiest foods to eat every day?'
# q2 = 'Make a receipe with those foods that varies for each day of the week.'
# q3 = 'What is the amount of calories for each meal?'

# system_prompt = 'Answer as concisely as possible.'

# messages = [
#     {"role": "system", "content": system_prompt},
#     {"role": "user", "content": q1},
#     {"role": "user", "content": q2},
#     {"role": "user", "content": q3}
# ]

# response = openai.chat.completions.create(
#     model = MODEL,
#     messages=messages,
#     temperature=0.7

# )

# bot_responce_1 = response.choices[0].message.content

# print(bot_responce_1)
# print()
# print('-' * 50)
# print()

# #Q2
# messages = [
#     {"role": "system", "content": system_prompt},
#     {"role": "user", "content": q1},
#     {"role": "assistant", "content": bot_responce_1},
#     {"role": "user", "content": q2}
# ]

# response = openai.chat.completions.create(
#     model = MODEL,
#     messages=messages,
#     temperature=0.7
# )

# bot_responce_2 = response.choices[0].message.content
# print(bot_responce_2)
# print()
# print('-' * 50)
# print()

# #Q3
# messages = [
#     {"role": "system", "content": system_prompt},
#     {"role": "user", "content": q1},
#     {"role": "assistant", "content": bot_responce_1},
#     {"role": "user", "content": q2},
#     {"role": "assistant", "content": bot_responce_2},
#     {"role": "user", "content": q3}
# ]

# response = openai.chat.completions.create(
#     model = MODEL,
#     messages=messages,
#     temperature=0.7
# )

# bot_responce_3 = response.choices[0].message.content
# print(bot_responce_3)

# questions = list()
# bot_responces = list()
# messages = list()
# system_prompt = input('System Prompt:')
# if system_prompt == '':
#     system_prompt = '''You answer briefly without further elaboration. If you don't know the answer we'll resond: "I don't know"'''
    
# print()

# messages.append({"role": "system", "content": system_prompt})

# def getSentiment(prompt, emotions):
#     system_prompt = f'''You are an emotionally intelligent assistant.
#     Classify the sentiment of user's text with ONLY ONE OF THE FOLLOWING EMOTIONS: {emotions}.
#     After classifying the text, respond with the emotion ONLY.'''
#     response = client.chat.completions.create(
#         model = MODEL,
#         messages = [
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens = 20,
#         temperature = 0.0
#     )