import streamlit as st
from typing import Literal
from dataclasses import dataclass
# from llm_model import get_qa_chain, create_vector_db
import streamlit.components.v1 as components
from langchain_core.messages import HumanMessage, AIMessage
st.set_page_config(page_title="Chatbot", page_icon="🖋")

# def history():
#     return st.session_state.chat_history

st.title("Chat-bot Guided Virtual Tour Of Uskt 📖")
# btn = st.button("Create Knowledgebase")
# if btn:
#     create_vector_db()


# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# #conversation

# for message in st.session_state.chat_history:
#     if isinstance(message, HumanMessage):
#         with st.chat_message("Human"):
#             st.markdown(message.content)
#     else:    
#         with st.chat_message("AI"):
#             st.markdown(message.content)
            
        

# user_query = st.chat_input()

# if user_query is not None and user_query !="":
#     st.session_state.chat_history.append(HumanMessage(user_query))

#     with st.chat_message("Human"):
#         st.markdown(user_query)

    
#     with st.chat_message("AI"):
#         chain = get_qa_chain()

#         try:
#             ai_response = chain(user_query + "?")
#             st.markdown(ai_response["result"])
#             # print(response["result"])
#         except IndexError as e:
#             # print(f"An error occurred: {e}")
#             # print("The LLM response was empty or malformed.")
#             st.markdown("An error occurred: {e}")
#         except Exception as e:
#             # print(f"An unexpected error occurred: {e}")
#             st.markdown(f"An unexpected error occurred: {e}")

            
#         # st.markdown(ai_response)
#         #Hi
#         #this is to update ai message in chat-history
#     st.session_state.chat_history.append(AIMessage(ai_response["result"]))