import streamlit as st
from openai import OpenAI
import os

st.title("Week 3 homework")

prompt = st.text_input("Share with us your experience of the latest trip")

### Load your API Key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAIKEY"]


from langchain.llms import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate


### Create the LLM API object
llm = OpenAI(openai_api_key=st.secrets["OPENAIKEY"])

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

airline_chain = PromptTemplate.from_template(
    """You are a customer agent for an airline. \
Determine if the cause of customer's dissatisfaction is the airline's fault. 
Do not respond with any reasoning. Just respond professionally as a customer service agent. Respond in first-person mode.

Your response should follow these guidelines:
    1. Do not provide any reasoning behind the customer's dissatification. Just respond professionally as a customer agent.
    2. Address the customer directly



Text:
{text}

"""
) | llm
