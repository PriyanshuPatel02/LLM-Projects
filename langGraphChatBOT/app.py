import os
from openai import OpenAI

# ✅ Set your Groq API key
# os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)

response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        # {"role": "user", "content": "Explain LangGraph in simple words"},

            {"role": "system", "content": "You are a helpful assistant that explains things in simple Hindi-English mix."},
        {"role": "user", "content": "LangGraph kya hota hai?"},
        {"role": "assistant", "content": "LangGraph ek framework hai jo AI workflows build karne ke liye use hota hai."},
        {"role": "user", "content": "Mujhe example ke sath samjhao please."},
        # {"role" : "user", "content" : "funny jokes batao lekin english mein"}


    ],
)

print(response.choices[0].message.content)


# Role	Use Case
# system	Set karta hai behavior ("You're a polite teacher")
# user	User ke messages
# assistant	Assistant ke purane responses for memory (very useful!)



#How to run this code >>>>>>>
# python app.py
