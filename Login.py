import streamlit as st
import redis
import datetime

PORT = 6379
HOST = "localhost"
DATE_FORMAT = '%y/%m/%d'

st.set_page_config(page_title="Login")
r = redis.Redis(host=HOST, port=PORT, decode_responses=True)
st.title('Login / Signup')
tab1, tab2 = st.tabs(["Login", "SignUp"])

with tab1: 
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
    
    if submit_button:
        stored_password = r.hget(username, "password")
        if stored_password == password:
            st.success("Login successful!")
            st.session_state['username'] = username
            choice = "Expense Tracker"
        else:
            st.error("Invalid username or password.")

with tab2:
    st.subheader("SignUp Section")
    with st.form("my_form"):
        username = st.text_input("User Name")
        password = st.text_input("Password",type='password')
        email = st.text_input("Email")
        dob = st.date_input("DOB", datetime.date.today(), max_value=datetime.date.today(), min_value = datetime.date(1950,1,1))
        gender = st.radio("Gender", ('Male', 'Female', 'Other'))
        city = st.text_input('City')
        submitted = st.form_submit_button("Submit")
    if submitted:
        if r.exists(username):
            st.error("Username already exists. Please choose a different username.")
        else:
            user_data = {
                "password": password,
                "city": city,
                "dob": dob.strftime(DATE_FORMAT),
                "gender": gender,
                "email": email,
            }
            r.hset(username, mapping=user_data)
            st.success("Signup successful. You can now login.")


