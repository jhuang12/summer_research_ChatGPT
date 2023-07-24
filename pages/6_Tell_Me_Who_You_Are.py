import streamlit as st
import datetime
import redis
from streamlit_extras.switch_page_button import switch_page


def showPage():
    user_survey = r.hgetall(f"{st.session_state['username']}:survey")
    with st.form("my_form"):
        
        st.subheader("Income")
        income = st.number_input("What is the total amount of income you expect to receive each month?", value = 0 if not user_survey else float(user_survey.get('income')))
        
        st.subheader("Fixed Expenses")
        rent = st.number_input("Rent/Mortgage",  value = 0 if not user_survey else float(user_survey.get('rent')))
        loan_payments = st.number_input("Loan Payments",  value = 0 if not user_survey else float(user_survey.get('loan')))
        insurance_premiums = st.number_input("Insurance Premiums",  value = 0 if not user_survey else float(user_survey.get('insurance')))
        utilities = st.number_input("Utilities (Electricity, water, gas, sewer services)",  value = 0 if not user_survey else float(user_survey.get('utilities')))
        internet_phone = st.number_input("Internet and Phone Bills",  value = 0 if not user_survey else float(user_survey.get('internet_phone')))
        subscriptions = st.number_input("Subscriptions (streaming platforms, magazine subscriptions, gym memberships etc)", value = 0 if not user_survey else float(user_survey.get('subscriptions')))
        hoa = st.number_input("HOA", value = 0 if not user_survey else float(user_survey.get('hoa')))
        childcare_tuition = st.number_input("Childcare/Tuition",  value = 0 if not user_survey else float(user_survey.get('childcare_tuition')))
        medical = st.number_input("Medical Expenses", value = 0 if not user_survey else float(user_survey.get('medical')))
        transport = st.number_input("Transportation Costs", value = 0 if not user_survey else float(user_survey.get('transport')))

        st.subheader("Variable Expenses")
        groceries = st.number_input("Groceries", value = 0 if not user_survey else float(user_survey.get('groceries')))
        dining = st.number_input("Dining out", value = 0 if not user_survey else float(user_survey.get('dining')))
        entertainment= st.number_input("Entertainment (Movies, concerts, events etc)", value = 0 if not user_survey else float(user_survey.get('entertainment')))
        shopping = st.number_input("Shopping", value = 0 if not user_survey else float(user_survey.get('shopping')))
        travel = st.number_input("Travel (Vacations, weekend getaways etc)", value = 0 if not user_survey else float(user_survey.get('travel')))
        gifts_donation = st.number_input("Gifts and donations", value = 0 if not user_survey else float(user_survey.get('gifts_donation')))
        health = st.number_input("Health and Wellness", value = 0 if not user_survey else float(user_survey.get('health')))
        personal_care = st.number_input("Personal Care (Haircuts, skincare products, salon services etc)", value = 0 if not user_survey else float(user_survey.get('personal_care')))
        hobbies = st.number_input("Hobbies and Interests", value = 0 if not user_survey else float(user_survey.get('hobbies')))

        st.subheader("Savings and Emergency Fund")
        savings = st.number_input("How much would you like to allocate to savings each month?", value = 0 if not user_survey else float(user_survey.get('savings')))

        st.subheader("Financial Goals")
        goals = st.text_area("Financial goals", value = "" if not user_survey else user_survey.get('goals'))

        st.subheader("What is the object for this session?")
        save_money = st.checkbox("I want to save money", value = False if not user_survey or user_survey.get('save_money') == "False" else True)
        increase_income = st.checkbox("I want to increase my income", value = False if not user_survey or user_survey.get('increase_income') == "False" else user_survey.get('increase_income'))
        understand_finance = st.checkbox("I want to understand a financial concept", value = False if not user_survey or user_survey.get('understand_finance') == "False" else user_survey.get('understand_finance'))
        know_procedure = st.checkbox("I want to know a procedure", value = False if not user_survey or user_survey.get('know_procedure') == "False" else user_survey.get('know_procedure'))

        if st.form_submit_button("Submit"):
            user_data = {
                "income": income,
                "rent": rent,
                "loan": loan_payments,
                "insurance": insurance_premiums,
                "utilities": utilities,
                "internet_phone": internet_phone,
                "subscriptions": subscriptions,
                "hoa": hoa,
                "childcare_tuition": childcare_tuition,
                "medical" : medical,
                "transport" : transport,
                "groceries" : groceries,
                "dining" : dining,
                "entertainment": entertainment,
                "shopping": shopping,
                "travel": travel,
                "gifts_donation": gifts_donation,
                "health": health,
                "personal_care": personal_care,
                "hobbies" : hobbies,
                "savings": savings,
                "goals" : goals,
                "save_money" : str(save_money),
                "increase_income" : str(increase_income),
                "understand_finance": str(understand_finance),
                "know_procedure" : str(know_procedure)
                }
            r.hset(f"{st.session_state['username']}:survey", mapping = user_data)
            st.success("Information Saved Successfully at "+str(datetime.datetime.now().strftime('%Y-%m-%d, %H:%M')))

PORT = 6379
HOST = "redis"
DATE_FORMAT = '%y/%m/%d'

st.set_page_config(page_title="Tell Me Who You Are")
r = redis.Redis(host=HOST, port=PORT, decode_responses=True)
st.title('Tell Me Who You Are')

if 'username' not in st.session_state:
    st.text("Please Login")
    if st.button("Login"):
        switch_page("Login")
else:
    username = st.session_state['username']
    showPage()
