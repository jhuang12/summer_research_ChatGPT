import streamlit as st
import redis
import pandas as pd
import datetime
import json
from streamlit_extras.switch_page_button import switch_page

PORT = 6379
HOST = "redis"
DATE_FORMAT = '%y/%m/%d'

st.set_page_config(page_title="Expense Tracker")
r = redis.Redis(host=HOST, port=PORT, decode_responses=True)
st.title('Expense Tracker')

if 'username' not in st.session_state:
    st.text("Please Login")
    if st.button("Login"):
        switch_page("Login")
else:
    with st.form("expense_tracker"):
        category = st.selectbox("Category", (
            "Groceries",
            "Dining/Restaurants",
            "Transportation",
            "Utilities",
            "Rent/Mortgage",
            "Insurance",
            "Entertainment",
            "Travel/Vacation",
            "Clothing/Apparel",
            "Personal Care",
            "Education",
            "Healthcare/Medical expenses",
            "Home Maintenance/Repairs",
            "Subscriptions",
            "Gifts/Donations",
            "Miscellaneous/Other"
        ))
        description = st.text_input("Note")
        expense_date = st.date_input("Date", datetime.date.today(), max_value=datetime.date.today(), min_value = datetime.date(1950,1,1))
        amount = st.number_input('Amount')
        submit_button = st.form_submit_button("Add")

    if submit_button:
            expense_id = r.incr(f"{st.session_state['username']}:counter")
            expense_data = {
                "Category": category,
                "Description": description,
                "Date" : expense_date.strftime(DATE_FORMAT),
                "Amount": amount,
            }
            r.hset(f"{st.session_state['username']}:expenses", expense_id, json.dumps(expense_data))
            st.success("Added")
    
    expense_entries = r.hgetall(f"{st.session_state['username']}:expenses")
    if expense_entries:
        st.subheader("Expense Entries")

        expense_data = []
        for expense_id, expense_entry in expense_entries.items():
            expense_entry = json.loads(expense_entry)
            expense_data.append(expense_entry)
        df = pd.DataFrame(expense_data)
        st.dataframe(df)


