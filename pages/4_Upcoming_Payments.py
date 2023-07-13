import streamlit as st
import pandas as pd
import redis
import datetime
import json
from streamlit_extras.switch_page_button import switch_page

PORT = 6379
HOST = "localhost"
DATE_FORMAT = '%y/%m/%d'

st.set_page_config(page_title="Upcoming Payments")
r = redis.Redis(host=HOST, port=PORT, decode_responses=True)

def findDay(date, date_list):
    day = datetime.datetime.strptime(date, DATE_FORMAT).weekday()
    for d in date_list:
        if datetime.datetime.strptime(d, DATE_FORMAT).weekday() == day:
            return d

if 'username' not in st.session_state:
    st.text("Please Login")
    if st.button("Login"):
        switch_page("Login")
else:
    st.title('Add Recurring Event')
    with st.form("recurring_event"):
        event_name = st.text_input("Event Name")
        start_date = st.date_input("Start Date", min_value=datetime.datetime.today())
        recurring = st.selectbox("Repeat", options=["Once","Daily", "Weekly", "Monthly","Yearly"])
        amount = st.number_input("Amount")
        submitted = st.form_submit_button("Add Event")

    if submitted:
        event_id = r.incr(f"{st.session_state['username']}:counter")
        event_data = {
                    "Event Name": event_name,
                    "Start Date" : start_date.strftime(DATE_FORMAT),
                    "Recurring": recurring,
                    "Amount": amount}
        r.hset(f"{st.session_state['username']}:events", event_id, json.dumps(event_data))
        st.success("Added")

    st.title('Upcoming Payments')
    base = datetime.datetime.today()
    date_list = [(base + datetime.timedelta(days=x)).strftime(DATE_FORMAT) for x in range(7)]
    event_date_list = {}

    for date in date_list:
        event_date_list[date] = []

    events = r.hgetall(f"{st.session_state['username']}:events")

    for event_id, event_entry in events.items():
        event_entry = json.loads(event_entry)
        
        if event_entry.get("Recurring") == "Once":
            if event_entry.get('Start Date') in date_list:
                event_date_list[date].append(event_entry.get("Event Name"))
        
        elif event_entry.get("Recurring") == "Daily":
            for date in date_list:
                event_date_list[date].append(event_entry.get("Event Name") + "\nAmt: " + str(event_entry.get("Amount")))

        elif event_entry.get("Recurring") == "Weekly":
            event_date_list[findDay(event_entry.get('Start Date'), date_list)].append(event_entry.get("Event Name"))

        elif event_entry.get("Recurring") == "Monthly":
            date = base.strftime('%y/%m') + "/" + event_entry.get('Start Date').split("/")[2]
            if date in date_list:
                event_date_list[date].append(event_entry.get("Event Name"))
            
        else:
            date = base.strftime('%y/%m') + "/" +event_entry.get('Start Date').split("/", 1)[1]
            if date in date_list:
                event_date_list[date].append(event_entry.get("Event Name"))

    max_list_length = max(len(lst) for lst in event_date_list.values())

    for key, value in event_date_list.items():
        if len(value) < max_list_length:
            value.extend([''] * (max_list_length - len(value)))

    st.dataframe(pd.DataFrame.from_dict(event_date_list))










