import streamlit as st
from openai import OpenAI
import os

st.title("Week 3 homework")

prompt = st.text_input("Share with us your experience of the latest trip")

### Load your API Key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAIKEY"]

### OpenAI stuff: Creative: High temperature
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  temperature = 1.8,
  max_tokens=20
)

### Display
st.write(
    "Creative: " + response.choices[0].message.content
)
