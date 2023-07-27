import openai
import os
import constant

#setup environment key - https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety

openai.api_key  = constant.openai_key

#reference: https://github.com/ralphcajipe/chatgpt-prompt-engineering/blob/main/7-chatbot.ipynb


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=1):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

#one way to create prompt
# %s - name, age, professon, city, country, goal and questions for the chatbot
# This is the first prompt with all the information that we collected from the users
prompt1 = f"""
Hi, my name is %s. I am a %s year old %s who are living in %s, %s. I want to %s. Could you help?' %('Elisa', '26', 'student', 'Seattle', 'USA', 'create a budget with $1200 to maximize my expense power')
"""

#another way to use massage for prompting
# messages =  [  
# {'role':'system', 'content':'You are a chatbot served as a financial advisor expert with user-friend, simple, concise and customer-centric tone. Please check the answers to ensure the accuracy and find quotes and references online before displaying the answers. Please use line breaks for each paragraph if needed.'},    
# {'role':'user', 'content':'Hi, my name is %s. I am a %s year old %s who are living in %s, %s. I want to %s. Could you help?' %('name', '26', 'student', 'Seattle', 
# 'USA', 'create a budget with $1200 to maximize my expense power')}  ]
# response = get_completion_from_messages(messages, temperature=1)

messages =  [  
{'role':'system', 'content':'You are a chatbot served as a financial advisor expert with user-friend, simple, concise and customer-centric tone. Please check the answers to ensure the accuracy and find quotes and references online before displaying the answers. Please use line breaks for each paragraph if needed.'},    
{'role':'user', 'content': prompt1}  ]

response = get_completion_from_messages(messages, temperature=1)

print(response)

#what are we going to do with a followup prompt? Maybe add a prompt2 for the followup. Then, we will need a logic to get the flow. 