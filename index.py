import streamlit as st
import datetime

st.title('Student Financial Planner')
# data = yaml.safe_load(open("countries+states+cities.yml","r"))

with st.form("my_form"):
   dob = st.date_input("DOB", datetime.date.today(), max_value=datetime.date.today(), min_value = datetime.date(1950,1,1))
   gender = st.radio("Gender", ('Male', 'Female', 'Other'))
   city = st.text_input('City')
   financial_knowledge = gender = st.radio("How would you evaluate your financial knowledge?", 
                                    ('Very good', 'Good', 'Fair', 'Not good', 'Poor'))
   is_international = st.radio("Are you an international student?", ('Yes', 'No'))
   school = st.text_input('Which school are you expecting to enroll?')
   program = st.text_input('What program are you expecting to enroll?')
   major = st.text_input('What major are you expecting to enroll?')
   speciality = st.text_input('What specialty are you expecting to enroll?')
   term = st.selectbox('Which term are you expecting to enroll in?',('Fall', 'Spring', 'Winter'))
   year = st.text_input('Enrollment year')
   submitted = st.form_submit_button("Submit")

st.text("Which of the following topics do you need help with?")
is_student_loan = st.checkbox("Student Loan")
is_financial_aid = st.checkbox("Financial Aid")
is_scholarship_grant = st.checkbox("Scolarship and Grant")
is_financial_budget = st.checkbox("Financial Budget")
if is_financial_budget:
    st.slider('What is you budget?', 0, 10000, 25)
is_bank_account = st.checkbox("Opening a Bank Account")
is_creditcard = st.checkbox("Credit Card Recommendation")
get_info = st.button("OK")

if get_info:
    tab = []
    tab_data = {"Student Loan" : is_student_loan, 
                "Financial Aid" : is_financial_aid,
                "Scholarship & Grants" : is_scholarship_grant,
                "Financial Budget" : is_financial_budget,
                "Bank" : is_bank_account,
                "Credit Card" : is_creditcard}

    for key, value in tab_data.items():
        if value:
            tab.append(key)
    tabs = st.tabs(tab)
       


