import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

# API Key input
# api_key = st.text_input("Enter your api key", value="", key=None)
api_key = st.secrets["API_KEY"]

# Api Key
API_KEY= api_key

# Initialize client
client = genai.Client(api_key=API_KEY)

# Title
st.title("Gemini App")

# Select the use
select_use = st.selectbox("Select your use:", ["Student", "Business"])

# Selected use: Student
if select_use == 'Student':
    
    # User input
    user_input=st.text_input("enter your prompt:")
    
    # Explain like I am 5
    st.info("ELI5 -> Explain like I am 5")
    option1 = st.selectbox("How do you want me to explain the concept?", ["ELI5", "Middle School", "High School", "College", "Expert"], index=None)
    if option1 == 'ELI5':
        response1 = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=user_input,
            config=types.GenerateContentConfig(
                system_instruction="You are given a prompt. You need to explain to the user the concept like he is a 5 year old. Explain it in detail if needed. Ask him if he understand it if not then explain him in a more easy way."
            )
        )
        st.markdown(response1.text)
        explaination = st.text_input("Did you understand the concept?")
        while explaination != 'satisfied':
            response2 = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=user_input,
                config=types.GenerateContentConfig(
                    system_instruction="The prior explanation was not good enough for user. Explain the concept more easier than your prior explanation!"
                )
            )
    # Middle School
    elif option1 == 'Middle School':
        response1 = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=user_input,
            config=types.GenerateContentConfig(
                system_instruction="You are given a prompt. You need to explain to the user the concept like he is in middle school. Explain it in detail if needed."
            )
        )
        st.markdown(response1.text)
    # High School
    elif option1 == 'High School':
        pass
    # College
    elif option1 == 'College':
        pass
    # Expert
    else:
        pass
        
    # Saving to file
    save = st.button("Do you want to save the output?", key=True)
    if save == 'Yes':
        with open("output.md", "w") as f:
            f.write(response1.text)
        

if select_use == 'Business':
    pass