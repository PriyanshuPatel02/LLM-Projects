

#TOOLs
# Tools are an incredibly powerful feature by the frontier LLMs
#With tools, you can write a function, and have the LLM call that function as part of its response. 
#Sounds almost spooky.. we're giving it the power to run code on our machine?

# ticket_prices = {"london": "$799", "paris": "$899", "tokyo": "$1400", "berlin": "$499"}
# def get_ticket_price(destination_city):
#     print(f"Tool get_ticket_price called for {destination_city}")
#     city  = destination_city.lower()
#     return ticket_prices.get(city, "Unknown")



import os
import json
from dotenv import load_dotenv
import gradio as gr
from langchain_groq import ChatGroq
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType

load_dotenv()

# ---------------- LLM Setup ----------------
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"
)

# ---------------- Tool Setup ----------------
ticket_prices = {"london": "$799", "paris": "$899", "tokyo": "$1400", "berlin": "$499"}

@tool
def get_ticket_price(destination_city: str) -> str:
    """Look up the ticket price for a given destination city."""
    print(f"Tool get_ticket_price called for {destination_city}")
    city = destination_city.lower()
    return ticket_prices.get(city, "Unknown")

tools = [get_ticket_price]

# ---------------- Agent Setup ----------------
system_message = (
    "You are a helpful assistant for an Airline called Flight. "
    "If the user asks for a ticket price to a city, ALWAYS use the tool `get_ticket_price` "
    "instead of guessing. Do not invent prices. "
    "Give short, courteous answers, no more than 2 sentences. "
    "If you don't know the answer, say 'Unknown'."
)


agent = initialize_agent(
    tools=[get_ticket_price],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,  # function-calling style agent
    verbose=True
)



# ---------------- Chat Function ----------------
def chat(message, history):
    response = agent.run(message)
    return response

# ---------------- Gradio UI ----------------
gr.ChatInterface(fn=chat).launch()




#There's a particular dictionary structure that's required to describe our function:
# price_function = {
#     "name": "get_ticket_price",
#     "description": "Get the price of a return ticket to the destination city. Call this whenever you need to know the
#     "parameters":{
#        "type": "object",
#        "properties": {
#           "destination_city": {
#               "type": "string",
#               "description": "The city that the customer wants to travel to",
#         },
#      },
#         "required": ["destination_city"],
#         "additional Properties": False
# }
# }
