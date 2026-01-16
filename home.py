import streamlit as st
from google import genai
import time
import pandas as pd
import plotly.express as px
from groq import Groq

st.set_page_config(page_title="LLM Benchmarking", layout="wide")
st.title("LLM Benchmarking Dashboard")
st.subheader("Compare as many LLMs as you want")
st.divider()

client = genai.Client(api_key="")
groq_client = Groq(api_key="")

# Function to call GenAI model
def call_genai_model(model_name, prompt):
    start = time.time()
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt )
    end = time.time()
    
    if response.usage_metadata:
        tokens_used = response.usage_metadata.total_tokens
    else:
        tokens_used = len(response.text) // 4
    return response.text, end - start, tokens_used


# Function to call Groq Llama model
def call_llama_model(model_name, prompt):
    start = time.time()
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7, 
    )
    end = time.time()
    
    response_text = response.choices[0].message.content
    tokens_used = response.usage.total_tokens
    return response_text, end - start, tokens_used