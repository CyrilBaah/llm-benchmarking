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

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Function to call GenAI model
def call_genai_model(model_name, prompt):
    start = time.time()
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt )
    end = time.time()
    
    if response.usage_metadata:
        tokens_used = response.usage_metadata.total_token_count
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

# Sidebar for model selection
with st.sidebar:
    st.header("Choose your models")
    use_genai = st.checkbox("Use GenAI Gemini-2.5-flash", value=True)
    use_llama = st.checkbox("Use Groq Llama-3.1-8b-instant", value=True)

prompt = st.chat_input("Enter your prompt here:")

if prompt:
    comparisons = []
    if use_genai:
        comparisons.append("GenAI Gemini-2.5-flash")
    if use_llama:
        comparisons.append("Groq Llama-3.1-8b-instant")

    cols = st.columns(len(comparisons))
    results = []

    for i, model in enumerate(comparisons):
        with cols[i]:
            st.subheader(model)
            if model == "GenAI Gemini-2.5-flash":
                response_text, latency, tokens_used = call_genai_model(model, prompt)
            elif model == "Groq Llama-3.1-8b-instant":
                response_text, latency, tokens_used = call_llama_model(model, prompt)
            
            st.caption(f"Latency: {latency:.2f} seconds | Tokens used: {tokens_used}")
            st.write(response_text)

            if latency > 0:
                results.append({
                    "Model": model,
                    "Latency (s)": latency,
                    "Tokens Used": tokens_used,
                    "Throughput (tokens/s)": tokens_used / latency
                })
    
    # Display comparison metrics
    if results:
        st.divider()
        st.subheader("Performance Comparison")
        
        df = pd.DataFrame(results)
        
        # Display metrics table
        st.dataframe(df, use_container_width=True)
        
        # Create visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            fig_latency = px.bar(df, x="Model", y="Latency (s)", 
                                title="Response Latency",
                                color="Model")
            st.plotly_chart(fig_latency, use_container_width=True)
        
        with col2:
            fig_throughput = px.bar(df, x="Model", y="Throughput (tokens/s)", 
                                   title="Throughput (tokens/s)",
                                   color="Model")
            st.plotly_chart(fig_throughput, use_container_width=True)