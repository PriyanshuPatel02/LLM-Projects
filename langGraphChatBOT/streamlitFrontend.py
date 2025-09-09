import streamlit as st
from langgraphBackend import chatbot
from langchain_core.messages import HumanMessage

# ***********  BASIC *********
# with st.chat_message('user'):
#     st.text('Hi')

# with st.chat_message('assistant'):
#     st.text('How can i assist yopu today?')    


# with st.chat_message('user'):
#     st.text('Explain me the concept of black hole?')      

# user_input = st.chat_input('Write something...') 

# if user_input :
#     with st.chat_message('user'):
#         st.text(user_input)

# ********** END ***********
# streamlit run streamlitFrontend.py








# message_history = []  # yeh msg store ke liye kiye hai

# {'role' : 'user', 'content' : 'Hi'}
# {'role' : 'assistant' , 'content' : 'Hello'}

CONFIG = {'configurable' : {'thread_id' : 'thread-1'}}  

if 'message_history' not  in st.session_state :
    st.session_state['message_history'] = [] #session state ke andar key mera messHistory hai jo vacent list h

#loading the convo history
for message in st.session_state['message_history']:  # har dictonary me dekh rhe
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input = st.chat_input('Write something...')

if user_input :

 # first add the message to message_history
    st.session_state['message_history'].append({'role' : 'user', 'content' : user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages' :[HumanMessage(content=user_input)]}, config= CONFIG)   #user ka msg  ayega usko humanMsg me convrt krenge
    ai_message = response['messages'][-1].content  # last msg return krenge
        
 # first add the message to mesHistory
    st.session_state['message_history'].append({'role' : 'assistant', 'content' :  ai_message }) 
    with st.chat_message('assistant'):
        # st.text( ai_message )    
        st.markdown(ai_message)    # line breaks, formatting, and multi-line text rendering beautifully.