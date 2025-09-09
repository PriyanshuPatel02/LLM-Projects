import os
import json
from dotenv import load_dotenv
import gradio as gr
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()


#initalization
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')
# MODEL = 'gpt-4o-mini'
# openai = OpenAI()


GROQ_API_KEY = os.environ.get("GROQ_API_KEY") 
llm = ChatGroq(
    # base_url="https://api.groq.com/openai/v1",       # ✅ Groq base URL
    api_key=os.getenv("GROQ_API_KEY"),             # ✅ Groq API Key in .env
    model="llama3-70b-8192"                           # ✅ Supported model
)

system_message = " You are a helpful assistant for an Airline called flight."
system_message += " Give short, courteous answers, no more than 2 sentence."
system_message += ' Always be accurate. If you dont know the answer, say no.'

def chat(message, history):
    messages = [{"role" : "system", "content" : system_message}]
    for human, assistant in history:
        messages.append({"role" : "user", "content" : system_message})
        messages.append({"role" : "assistant", "content" : assistant})

    messages.append({"role" : "user", "content" : message})
    # response = openai.chat.completions.create(model= MODEL, messages = messages)
    # return response.choice[0].message.content  

    response = llm.invoke(messages)  # LangChain way
    return response.content

gr.ChatInterface(fn=chat).launch()