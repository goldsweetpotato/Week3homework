import streamlit as st
from openai import OpenAI
import os

st.title("Week 3 homework")

prompt = st.text_input("Share with us your experience of the latest trip")

### Load your API Key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAIKEY"]

### Create the LLM API object
llm = OpenAI(openai_api_key=st.secrets["OPENAIKEY"])

from langchain.llms import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate

experience_template = """You are a customer agent for an airline.
From the following text, determine whether the customer had a negative experience or not.

Do not respond with more than one word.

Text:
{request}

"""


### Create the decision-making chain

exprience_type_chain = (
    PromptTemplate.from_template(experience_template)
    | llm
    | StrOutputParser()
)
