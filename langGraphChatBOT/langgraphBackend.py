from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message  import add_messages
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
import os

load_dotenv()

llm = ChatOpenAI(
     base_url="https://api.groq.com/openai/v1",       # ✅ Groq base URL
    api_key=os.getenv("OPENAI_API_KEY"),             # ✅ Groq API Key in .env
    model="llama3-70b-8192"                           # ✅ Supported model
)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state : ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages" : [response]}


# Checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

# stream = chatbot.stream(
#     {"messages" : [HumanMessage(content='What is the recipe to make maggie')]},
#     config= {'configurable' : {'thread_id' : 'thread-1'}},
#     stream_mode= 'messages'
# )

# print(type(stream))
