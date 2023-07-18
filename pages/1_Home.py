import streamlit as st
import redis
from streamlit_extras.switch_page_button import switch_page


PORT = 6379
HOST = "redis"

st.set_page_config(page_title="Home")
r = redis.Redis(host=HOST, port=PORT, decode_responses=True)

st.title('Hi Welcome - A quick intro to the tool😄')


if 'username' not in st.session_state:
    st.text("Please Login")
    if st.button("Login"):
        switch_page("Login")
else:
    st.write("This page will briefly introduce how you can use this tool to help you with your financial needs. Enjoy your exploration!")
    st.write(" ")
    st.markdown("**Step 1: Tell Me Who You Are**")
    if 'hasFilled' in st.session_state and st.session_state['hasFilled']:
        st.markdown("You already filled out the form! You don't have to sumbit one more time unless you want to update your answer.")
        st.markdown("Otherwise, you can skip to the Step 2!")
    else:
        st.markdown("This is really important. If we don't know who you are, we cannot help you!")
        st.markdown("So click `SUBMIT` tab on the left-side bar and complete it!")
        if st.button('Tell Me Who You Are'):
            switch_page("Tell Me Who You Are")
    st.write(" ")
    st.markdown("**Step 2: Choose what we can help?**")
    st.markdown("Click tab (eg. `Financial Budget`) on the sidebar or buttons below to go to each subpage. On each page you may have a few more questions")
    col1, col2, col3,  = st.columns(3)
    if col1.button('Expense Tracker'):
        switch_page("Expense Tracker")
    if col2.button('Financial Budget'):
        switch_page('Financial Budget')
    if col3.button('Upcoming Payments'):
        switch_page('Upcoming Payments')
    

