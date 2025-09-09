import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY") 
llm = ChatGroq(
    # base_url="https://api.groq.com/openai/v1",       # ✅ Groq base URL
    api_key=os.getenv("GROQ_API_KEY"),             # ✅ Groq API Key in .env
    model="llama3-70b-8192"                           # ✅ Supported model
)

system_message = " You are a helphul wonderful assistant"

def chat(message, history):
    # messages = [{"role": "system", "content" : system_message}]
    messages = [SystemMessage(content=system_message)]
  # Past conversation ko format karna
    for user_message, assistant_message in history:
        messages.append({"role" : "user", "content" : user_message})
        messages.append({"role": "assistant", "content" : assistant_message})
    
      # Abhi ka user message
    messages.append(HumanMessage(content=message))
    # messages.append({"role" : "user", "content" : message})


    print("History is : ")
    print(history)
  
    print("And messages is: ")
    print(messages)
    response = llm.invoke(messages)  # LangChain way
    return response.content

    # stream = llm.chat.completions.create (
    #     model = "llama3-70b-8192",
    #     messages = messages, 
    #     stream = True )   

    # response = ""
    # for chunk in stream : 
    #     response += chunk.choices[0].delta.content or ''
    #     yield response

app = gr.ChatInterface(fn=chat).launch()

if __name__ == "__main__":
    app.launch()
