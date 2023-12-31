import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))

# Streamlit UI elements
st.title("ConsultBot - A chatbot for practicing case studies - By Ayush Agarwal")

# Initial prompt for the model
initial_prompt = """
Pick a random case study from the given casebooks. Now act as the interviewer, and the user will be the interviewee. 
Help the user practice the case study question for consulting interviews. 
Remember that the approach and the numbers assumed by the interviewee could be different; you just have to judge 
on the basis of how the structured thinking skills of the interviewee are (where structured thinking can be judged from the 
example cases in the books), and you have to drive the interviewee to the same end result of the case. 
Your first message should be any random case study from the given knowledge base. You can keep the first question slightly ambiguous 
since we are also testing the interviewee on the basis of clarifying questions asked.
"""

# Send the initial prompt to the chatbot
url = f'http://{api_host}:{api_port}/'
data = {"query": initial_prompt}
initial_response = requests.post(url, json=data)

# Initialize state to keep track of conversation history
past_data = [initial_prompt, initial_response.json()]

# Display initial response
st.write("# Interviewer")
st.write(initial_response.json())

# Streamlit callback to handle user input
@st.cache_data()
def get_response(question):
    prompt = ""
    for msg in past_data:
        prompt += msg
    prompt += question
    data = {"query": prompt}
    response = requests.post(url, json=data)
    return response.json()

# Get user input
question = st.text_input(
    "Ur response plz",
    key="response",
    placeholder="Enter your response as an interviewee"
)

# Add a button to submit the response
submit_button = st.button("Submit Response")

# Handle button click event
if submit_button:
    # Get chatbot response and update conversation history
    response = get_response(question)
    st.write("# Interviewer")
    st.write(response)
    past_data.append(question)
    past_data.append(response)
