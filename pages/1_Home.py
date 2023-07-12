import streamlit as st
import redis

st.set_page_config(page_title="Home")

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
st.title('Budget Planner')