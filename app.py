import streamlit as st
from clarifai_utils.modules.css import ClarifaiStreamlitCSS

st.set_page_config(layout="wide")

ClarifaiStreamlitCSS.insert_default_css(st)
from langchain.llms import Clarifai

# title and side bar
st.title("Chat with Llama 2.0")

# get the Clarifi API Key
with st.sidebar:
    clarifai_pat = st.text_input("Clarifi API Key",type="password")


def generate(text):
    llms = Clarifai(pat=clarifai_pat,user_id='meta',app_id='llama-2',model_id='llma2-70b-chat')
    st.info(llms(text))

# Form that takes text as input and return the response from the model
with st.form('myform'):
    text=st.text_area('Enter the text',"How to evaluate the ML models?")
    submit=st.form_submit_button('Submit')
    if not clarifai_pat:
        st.info("Please add your clarifai PAT to continue")
    elif  submit:
        generate(text)

# Footer   
# st.markdown("please select a specific page from the sidebar to the left")
