import streamlit as st
import datetime
import redis
import time
from streamlit_extras.switch_page_button import switch_page


def showPage():
    with st.form("my_form"):
        is_international = st.radio("Are you an international student?", ('Yes', 'No'))
        monthly_budget = st.number_input("Your montly budget in total")
        if_rent = st.radio("Will you pay the rent?", ('Yes', 'No'))
        if if_rent:
            rent = st.number_input("How much you wanna pay?")
        else:
            rent = 0
        

        if st.form_submit_button("Submit"):
            user_data = {
                "is_international": is_international,
                "monthly_budget": monthly_budget,
                "if_rent": if_rent,
                "rent": rent,
                }
            r.hset(username, mapping=user_data)
            time.sleep(0.5)
            st.success("Information Saved Successfully at "+str(datetime.datetime.now().strftime('%Y-%m-%d, %H:%M')))
            switch_page("Home")


PORT = 6379
HOST = "localhost"
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
