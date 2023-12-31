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

question = st.text_input(
    "What shall we practice today ? Initiate the discussion with the interviewer.",
    placeholder="Enter your response as an interviewee"
)


if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("# Interviewer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
