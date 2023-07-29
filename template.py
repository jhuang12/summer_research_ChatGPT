import openai
import os
import constant

#setup environment key - https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety

# openai.api_key  = constant.openai_key
openai.api_key = os.environ["OPENAI_API_KEY"]

#reference: https://github.com/ralphcajipe/chatgpt-prompt-engineering/blob/main/7-chatbot.ipynb

output_example = {
  "conservative expense": {
    "expense type": "conservative expense",
    "total monthly budget": "$14000",
    "housing cost": {
      "expense": "$2500",
      "percentage of total budget": "17.9%",
      "savings examples": [
        "Consider downsizing to a smaller, more affordable home or apartment",
        "Refinance your mortgage to get a lower interest rate"
      ],
      "spending examples": [
        "Rent or mortgage payment",
        "Property taxes",
        "Home insurance"
      ]
    },
    "utility": {
      "expense": "$600",
      "percentage of total budget": "4.3%",
      "savings examples": [
        "Cut back on energy usage by turning off lights and unplugging devices when not in use",
        "Shop around for better deals on internet, cable, and phone services"
      ],
      "spending examples": [
        "Electricity",
        "Water",
        "Internet"
      ]
    },
    "transportation": {
      "expense": "$1500",
      "percentage of total budget": "10.7%",
      "savings examples": [
        "Consider using public transportation, walking, or biking instead of owning a car",
        "Opt for carpooling or ride-sharing services to save on transportation costs"
      ],
      "spending examples": [
        "Public transportation fares",
        "Gas or car maintenance",
        "Insurance"
      ]
    },
    "grocery": {
      "expense": "$600",
      "percentage of total budget": "4.3%",
      "savings examples": [
        "Plan meals and shop with a grocery list to avoid impulsive purchases",
        "Buy generic or store-brand items instead of name brands"
      ],
      "spending examples": [
        "Food",
        "Toiletries",
        "Cleaning supplies"
      ]
    },
    "medical expenses": {
      "expense": "$800",
      "percentage of total budget": "5.7%",
      "savings examples": [
        "Use generic medications whenever possible",
        "Negotiate medical bills and explore options for lower-cost healthcare providers"
      ],
      "spending examples": [
        "Health insurance premiums",
        "Doctor visits",
        "Prescription medications"
      ]
    },
    "education": {
      "expense": "$400",
      "percentage of total budget": "2.9%",
      "savings examples": [
        "Look for scholarships, grants, or employer reimbursement programs for education expenses",
        "Consider online or community college courses as a more affordable option"
      ],
      "spending examples": [
        "Tuition",
        "Books",
        "Educational supplies"
      ]
    },
    "entertainment": {
      "expense": "$400",
      "percentage of total budget": "2.9%",
      "savings examples": [
        "Look for free or low-cost entertainment options, such as community events or outdoor activities",
        "Limit eating out and opt for homemade meals or packed lunches"
      ],
      "spending examples": [
        "Movies or streaming services",
        "Dining out",
        "Hobbies or recreational activities"
      ]
    },
    "savings": {
            "expense": "$4200",
            "percentage of total budget": "30%",
            "savings examples": ["Put money into a high-yield savings account", "Invest in low-risk options like bonds or certificates of deposit"],
            "spending examples": []
        },
    "other areas": {
      "expense": "$600",
      "percentage of total budget": "4.3%",
      "savings examples": [
        "Cut back on unnecessary expenses, such as subscription services or impulse purchases",
        "Review and negotiate bills, such as insurance and healthcare costs"
      ],
      "spending examples": [
        "Debt repayment",
        "Savings and investments",
        "Travel"
      ]
    }
  },
  "aggressive expense": {
    "expense type": "aggressive expense",
    "total monthly budget": "$12000",
    "housing cost": {
      "expense": "$2500",
      "percentage of total budget": "20.8%",
      "savings examples": [
        "Consider downsizing to a smaller, more affordable home or apartment",
        "Refinance your mortgage to get a lower interest rate"
      ],
      "spending examples": [
        "Rent or mortgage payment",
        "Property taxes",
        "Home insurance"
      ]
    },
    "utility": {
      "expense": "$600",
      "percentage of total budget": "5%",
      "savings examples": [
        "Cut back on energy usage by turning off lights and unplugging devices when not in use",
        "Shop around for better deals on internet, cable, and phone services"
      ],
      "spending examples": [
        "Electricity",
        "Water",
        "Internet"
      ]
    },
    "transportation": {
      "expense": "$1500",
      "percentage of total budget": "12.5%",
      "savings examples": [
        "Consider using public transportation, walking, or biking instead of owning a car",
        "Opt for carpooling or ride-sharing services to save on transportation costs"
      ],
      "spending examples": [
        "Public transportation fares",
        "Gas or car maintenance",
        "Insurance"
      ]
    },
    "grocery": {
      "expense": "$600",
      "percentage of total budget": "5%",
      "savings examples": [
        "Plan meals and shop with a grocery list to avoid impulsive purchases",
        "Buy generic or store-brand items instead of name brands"
      ],
      "spending examples": [
        "Food",
        "Toiletries",
        "Cleaning supplies"
      ]
    },
    "medical expenses": {
      "expense": "$1000",
      "percentage of total budget": "8.3%",
      "savings examples": [
        "Use generic medications whenever possible",
        "Negotiate medical bills and explore options for lower-cost healthcare providers"
      ],
      "spending examples": [
        "Health insurance premiums",
        "Doctor visits",
        "Prescription medications"
      ]
    },
    "education": {
      "expense": "$400",
      "percentage of total budget": "3.3%",
      "savings examples": [
        "Look for scholarships, grants, or employer reimbursement programs for education expenses",
        "Consider online or community college courses as a more affordable option"
      ],
      "spending examples": [
        "Tuition",
        "Books",
        "Educational supplies"
      ]
    },
    "entertainment": {
      "expense": "$400",
      "percentage of total budget": "3.3%",
      "savings examples": [
        "Look for free or low-cost entertainment options, such as community events or outdoor activities",
        "Limit eating out and opt for homemade meals or packed lunches"
      ],
      "spending examples": [
        "Movies or streaming services",
        "Dining out",
        "Hobbies or recreational activities"
      ]
    },
    "savings": {
            "expense": "$270",
            "percentage of total budget": "10%",
            "savings examples": ["Put money into a high-yield savings account", "Invest in low-risk options like bonds or certificates of deposit"],
            "spending examples": []
        },
    "other areas": {
      "expense": "$5900",
      "percentage of total budget": "49.2%",
      "savings examples": [
        "Cut back on unnecessary expenses, such as subscription services or impulse purchases",
        "Review and negotiate bills, such as insurance and healthcare costs"
      ],
      "spending examples": [
        "Debt repayment",
        "Savings and investments",
        "Travel"
      ]
    }
  }
}

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
Could you help create a monthly budget for me?' %('Alan', '55', 'professor', 'Iowa city', 'USA', '$5000', '$1000', 'maximize my expense power')

Your task is to create two budget plans based on the information above.
    A conservative expense plan is to use 70% of the monthly total budget and save 30% of the budget
    A agressive expense plan is to use 90% of the monthly total budget and save 10% of the budget 

    Monthly total budget is the net difference between monthly income and mortage and loan.

    Each plan covers 
        total monthly budget, housing cost, utility, transportation, grocery, medical expenses, education, entertainment and other areas.
    
    Each area above, give the following things:
        specific amount of expense, exact percentage of the total budget, and practical examples for savings and spendings for each category.
    
    Put the plan above into a json object that contains the 
        following keys: expense type (conservative or aggressive), total monthly budget, housing cost, utility, transportation, grocery, entertainment, saving and others
    
    Use format as {output_example} for the json output.
"""

messages =  [  
{'role':'system', 'content':'You are a chatbot served as a financial advisor expert only speaking JSON. Do not use normal text'},    
{'role':'user', 'content': prompt1}  ]

response = get_completion_from_messages(messages, temperature=1)

print(response)