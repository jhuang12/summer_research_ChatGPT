import openai

openai.api_key = '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'

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="What dinosaurs lived in the cretaceous period?",
  max_tokens=60
)

#openAI response text only
print(response.choices[0].text.strip())

##openAI response format full example
print(response)
