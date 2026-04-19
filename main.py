import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import os

load_dotenv()

st.set_page_config(page_title="Web Content Processor", layout="wide")

st.title("🌐 Site Mentor")

url = st.text_input("Enter Web URL", 
                    value="", placeholder="https://www.example.com/")

user_input = st.text_area(
    "What do you want to do with this web content?",
    value="",
    placeholder="Explain me like i'm 5 year old...or\nCreate me notes...or\nExplain me xyz topic...",
    height=150
)

run_btn = st.button("Process", help="If you encounter any error then just click again on button")

if run_btn:    
    if url == '' or user_input == '':
        st.write("Inputs can not be empty")
    else:
        try:
            with st.spinner("Processing..."):

                loader = WebBaseLoader(url)
                docs = loader.load()
                web_page_content = docs[0].page_content

                model = init_chat_model(
                    model=os.getenv("MODEL_NAME"),
                    model_provider=os.getenv("MODEL_PROVIDER")
                )

                SYSTEM_PROMPT = """
                You are an intelligent text processing assistant...
                """ 

                template = ChatPromptTemplate(
                    [
                        ("system", SYSTEM_PROMPT),
                        ("human", "{query}\n{text}")
                    ]
                )

                prompt = template.format_messages(
                    query=user_input,
                    text=web_page_content
                )

                response = model.invoke(prompt)
                result = response.content

            
                with open('./Tutor.md', 'w', encoding='utf-8') as file:
                    file.write(result)

            st.subheader("📄 Output")
            st.markdown(result)

            with open("./Tutor.md", "rb") as file:
                st.download_button(
                    label="Download Result",
                    data=file,
                    file_name="Tutor.md",
                    mime="text/markdown"
                )
        except Exception as e:
            st.write("Something went wrong...")