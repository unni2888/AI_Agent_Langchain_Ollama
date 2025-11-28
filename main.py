from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st
import re

template = """Question: {question}"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="deepseek-r1:1.5b")

chain = prompt | model

st.write("Hi, I'm your AI Agent")

# Use a form so pressing Enter in the text input submits like the Search button.
with st.form("search_form"):
    question = st.text_input("Enter your question:")
    submitted = st.form_submit_button("Search")

    if submitted and question:
        with st.spinner("Researching..."):
            result = chain.invoke({"question": question}, think=False)

            cleaned_content = re.sub(r"<think>.*?</think>\n?", "", result, flags=re.DOTALL)
            st.markdown(cleaned_content)
            st.write("------------------------------------------------------------")