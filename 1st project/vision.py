import streamlit as st
import os
import google.generativeai as genai

# Configure the API key for the Gemini model
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Error: GOOGLE_API_KEY is not set in the environment variables.")
    st.stop()

genai.configure(api_key=api_key)

# Function to get a response from the Gemini model
def get_gemini_response(input_text, image):
    try:
        if input_text and image:
            response = genai.generate_text(prompt=f"{input_text} Describe this image: {image}")
        elif input_text:
            response = genai.generate_text(prompt=input_text)
        elif image:
            response = genai.generate_text(prompt=f"Describe this image: {image}")
        else:
            return "No input provided."
        return response.candidates[0]['output'] if response.candidates else "No response generated."
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header('Gemini Application')
input_text = st.text_input("Input Prompt: ", key='input')

# File uploader for images
upload_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image = ""
if upload_file is not None:
    image = upload_file.name  # Use the file name as a placeholder
    st.image(upload_file, caption='Uploaded Image.', use_column_width=True)

submit = st.button('Tell me about this image')

# When the button is clicked, get the response from the model
if submit:
    response = get_gemini_response(input_text, image)
    st.subheader('The response is:')
    st.write(response)