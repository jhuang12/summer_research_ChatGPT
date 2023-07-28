import openai
import os
import constant

#setup environment key - https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety

# openai.api_key  = constant.openai_key
openai.api_key = os.environ["OPENAI_API_KEY"]

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
Hi, my name is %s. \n
I am a %s year old %s who are living in %s, %s. \n
My monthly income is %s.\n
My mortgage and loan is %s.\n
I want to %s. \n
Could you help create a monthly budget for me?' %('Elisa', '82', 'retiree', 'New York city', 'USA', '$15000', '$1000', 'maximize my expense power')

Your task is to create two budget plans based on the information above and use the difference between monthly income and mortage and loan.
    A conservative expense to maximize saving and a agressive expense to maximize expense saving
    Each plan covers 
        total monthly budget, housing cost, utility, transportation, grocery, entertainment and other areas.
    Each area above, give the following things:
        specific amount of expense, exact percentage of the total budget, and practical examples for savings and spendings for each category.
    Put the plan above into a json object that contains the 
        following keys: expense type (conservative or aggressive), total monthly budget, housing cost, utility, transportation, grocery, entertainment, areas that I can save for each category
"""

messages =  [  
{'role':'system', 'content':'You are a chatbot served as a financial advisor expert only speaking JSON. Do not use normal text'},    
{'role':'user', 'content': prompt1}  ]

response = get_completion_from_messages(messages, temperature=1)

print(response)