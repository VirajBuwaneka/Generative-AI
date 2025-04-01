from dotenv import load_dotenv
load_dotenv() ##Loading all the environmental variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## fUNCTION TO LOAD GEMINI MODEL
model=genai.GenerativeModel()
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#initialize our streamlit app
st.set_page_config(page_title="Q & A  Demo")
st.header('Gemini Application')
input=st.text_input("Input: ",key='input')
submit=st.button('Ask the question')


##when the button is clicked, we will get the response from the model

if submit:
    response=get_gemini_response(input)
    st.subheader('The response is: ')
    st.write(response)