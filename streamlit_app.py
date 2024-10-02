import streamlit as st
from openai import OpenAI
import os

st.title("Week 3 homework")

prompt = st.text_input("Share with us your experience of the latest trip")
