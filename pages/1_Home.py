import streamlit as st
import redis

PORT = 6379
HOST = "localhost"


st.set_page_config(page_title="Home")

r = redis.Redis(host=HOST, port=PORT, decode_responses=True)
st.title('Budget Planner')