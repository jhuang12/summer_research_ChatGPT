import streamlit as st
from streamlit import session_state as state
import matplotlib.pyplot as plt
from streamlit_chat import message
import OpenAIClient
import redis
import json
import openai
from streamlit_extras.switch_page_button import switch_page




def setPieData(labels, sizes):
    ax1.pie(sizes, labels=labels)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    


PORT = 6379
HOST = "redis"
DATE_FORMAT = '%y/%m/%d'

st.set_page_config(page_title="Financial Budget")
r = redis.Redis(host=HOST, port=PORT, decode_responses=True)
st.title('Financial Budget')


if 'username' not in st.session_state:
    st.text("Please Login")
    if st.button("Login"):
        switch_page("Login")
else:
        
    st.write("Looks like you are interested in making your own budget plan- Wonderful! I can help you with that.")
    st.write("Well- To better serve you, I need a few more information from your side. ")

    # 1/ TODO: Initiate Data from @Vrinda 
    fig1, ax1 = plt.subplots()


    # 2/ Page Component
    a1 = st.text_input('question 1')
    a2 = st.text_input('question 2')
    a3 = st.text_input('question 3')
    b1 = st.button("Continue")

    # 3/ TODO: Get the response from GPT Model @ Jialin 
        # ?: What data you need to get the expected data we want.
        # ?: Any API I can call?
    labels = [] 
    sizes = []
    if st.button("Get my chart!"):
        res = OpenAIClient.get_completion_from_messages()
        st.write('checkp1')
        json_dict = json.loads(res)["conservative expense"]
        
        for item, value in json_dict.items():
            if "percentage of total budget" in value:
                # st.write(item, value)
                labels.append(item)
                sizes.append(float(value["percentage of total budget"].rstrip('%')))
        # st.write(labels)
        # st.write(sizes)


        # st.write('here1')
        # st.write(not labels)
        # st.write(not sizes)
        # st.write(len(labels) == len(sizes))
        # Will parse the data from GPT Model and set data for pie chart.
        if labels and sizes and len(labels) == len(sizes):
            setPieData(labels, sizes)
            st.pyplot(fig1)


    with st.expander("Need more help?"):

        st.title("💬 HelpGPT")
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

        with st.form("chat_input", clear_on_submit=True):
            a, b = st.columns([4, 1])
            user_input = a.text_input(
                label="Your message:",
                placeholder="What would you like to say?",
                label_visibility="collapsed",
            )
            b.form_submit_button("Send", use_container_width=True)

        for idx, msg in enumerate(st.session_state.messages):
            message(msg["content"], is_user=msg["role"] == "user", key=idx)

        # we need to provide this key.
        if user_input and not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")

        if user_input and openai_api_key:
            openai.api_key = openai_api_key
            st.session_state.messages.append({"role": "user", "content": user_input})
            message(user_input, is_user=True)
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
            msg = response.choices[0].message
            st.session_state.messages.append(msg)
            message(msg.content)


    if "isSubmit" not in st.session_state:
        st.write("No information available, we cannot help you")
    else:
        st.write("TODO: May need more questions to this specific topic -> Generate Template based on information -> Send to ChatGPT -> Generate graphs/charts for visualization.")







