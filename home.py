import streamlit as st
from google import genai
import time
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="LLM Benchmarking", layout="wide")
st.title("LLM Benchmarking Dashboard")
st.subheader("Compare as many LLMs as you want")
st.divider()

