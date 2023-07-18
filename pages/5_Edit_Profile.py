import streamlit as st
import redis
import datetime
from streamlit_extras.switch_page_button import switch_page

PORT = 6379
HOST = "redis"
DATE_FORMAT = '%y/%m/%d'

st.set_page_config(page_title="Update Profile")
r = redis.Redis(host=HOST, port=PORT, decode_responses=True)

def getGender(g):
    if g.startswith('M'):
        return 0
    elif g.startswith('F'):
        return 1
    else: 
        return 2

st.title('Update Profile')

if 'username' not in st.session_state:
    st.text("Please Login")
    if st.button("Login"):
        switch_page("Login")

else: 
    user_details = r.hgetall(f"{st.session_state['username']}")
    with st.form("user_profile"):
        password = st.text_input("Password",type='password', value = user_details.get('password'))
        email = st.text_input("Email", value = user_details.get('email'))
        dob = st.date_input("DOB", datetime.datetime.strptime(user_details.get('dob'), DATE_FORMAT), max_value=datetime.date.today(), min_value = datetime.date(1950,1,1))
        gender = st.radio("Gender",('Male', 'Female', 'Other'), index = getGender(user_details.get('gender')))
        city = st.text_input('City', value = user_details.get('city')) 
        submitted = st.form_submit_button("Update")

    if submitted:
        user_data = {
                    "password": password,
                    "city": city,
                    "dob": dob.strftime(DATE_FORMAT),
                    "gender": gender,
                    "email": email,
                }
        r.hset(f"{st.session_state['username']}", mapping=user_data)                                                                            

    
