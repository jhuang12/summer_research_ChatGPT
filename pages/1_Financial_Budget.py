import streamlit as st
import datetime
from streamlit import session_state as state
import matplotlib.pyplot as plt
from streamlit_chat import message

def setPieData():
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [15, 30, 45, 10]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    ax1.pie(sizes, labels=labels)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    


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



# Will parse the data from GPT Model and set data for pie chart.
setPieData()


# Draw the picture
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


if not state.submitted:
    st.write("No information available, we cannot help you")
else:
    
    st.write("TODO: May need more questions to this specific topic -> Generate Template based on information -> Send to ChatGPT -> Generate graphs/charts for visualization.")







