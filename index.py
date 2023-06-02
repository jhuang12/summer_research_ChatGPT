import streamlit as st
import datetime

st.title('Student Financial Planner')

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
   st.text("Which of the following topics do you need help with?")
   is_student_loan = st.checkbox("Student Loan")
   is_financial_aid = st.checkbox("Financial Aid")
   is_scholarship_grant = st.checkbox("Scolarship and Grant")
   is_financial_budget = st.checkbox("Financial Budget")
   is_bank_account = st.checkbox("Opening a Bank Account")
   is_creditcard = st.checkbox("Credit Card Recommendation")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("hello")


