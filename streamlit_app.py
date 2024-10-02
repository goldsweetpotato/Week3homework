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

### Create the decision-making chain
experience_template = """You are a customer agent for an airline.
From the following text, determine whether the customer had a negative experience or not.

Do not respond with more than one word.

Text:
{prompt}

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
Do not respond with more than one word.

Text:
{prompt}

"""
) | llm

general_chain = PromptTemplate.from_template(
    """You are a customer agent for an airline.
    Given the text below, determine the length of the traveller's journey in hours.

    Your response should follow these guidelines:
    1. You should display a message offering sympathies and inform the user that customer service will contact them soon to resolve the issue or provide compensation.
    2. Do not respond with any reasoning. Just respond professionally as a custmer service agent.
    3. Address the customer directly

Text:
{prompt}

"""
) | llm


from langchain_core.runnables import RunnableBranch

### Routing/Branching chain
branch = RunnableBranch(
    (lambda x: "negative" in x["experience_type"].lower(), airline_chain
    ,
    general_chain,
)

### Put all the chains together
full_chain = {"experience_type": exprience_type_chain, "prompt": lambda x: x["prompt"]} | branch

import langchain
langchain.debug = False

full_chain.invoke(prompt)
