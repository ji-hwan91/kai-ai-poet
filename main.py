# from dotenv import load_dotenv
# load_dotenv()
import os
from langchain_openai import ChatOpenAI
import streamlit as st
import time
 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI()

st.title("인공지능 시인")

content = st.text_input("시의 주제를 적어주세요")
st.write("시의 주제는", content)

if content == "":
    print("")
else:
    with st.spinner("시 작성 중.."):
        response = chat_model.invoke(f"{content}에 대한 시를 써줘").content
    st.success(response)
