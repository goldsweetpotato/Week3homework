import streamlit as st
from openai import OpenAI
import os

st.title("My Super Awesome OpenAI API Deployment!")

prompt = st.text_input("What is your prompt today?", "Damascus is")
