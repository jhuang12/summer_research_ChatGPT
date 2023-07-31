import openai
import Constant

openai.api_key = Constant.openai_key

def get_completion_from_messages():
    response = openai.ChatCompletion.create(
        model=Constant.model,
        messages=Constant.messages,
        temperature=Constant.temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]