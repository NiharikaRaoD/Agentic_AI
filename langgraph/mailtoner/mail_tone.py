from typing import TypedDict
from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import START, END, StateGraph

class Email(TypedDict):
    Draft_Email: str
    Email_Tone: str
    Final_Email: str

load_dotenv()
model_name = os.getenv('MODEL_NAME')
model_provider = os.getenv('MODEL_PROVIDER')
llm = init_chat_model(model=model_name, model_provider=model_provider)

def change_email_tone(state: Email) -> Email:
    Draft_Email = state['Draft_Email']
    Email_Tone = state['Email_Tone']
    prompt = ChatPromptTemplate([
        ('system', 'You are an expert in writing emails'),
        ('user', 'Consider the following draft email {Draft_Email}. Preserve the meaning and do not change the facts.'),
        ('user', 'Rewrite the email in {Email_Tone} in less than 200 words')
    ])
    chain = prompt | llm
    response = chain.invoke({'Draft_Email': Draft_Email, 'Email_Tone':Email_Tone})
    state['Final_Email'] = response.content
    return state

emailtone_graph = StateGraph(Email)
emailtone_graph.add_node("Change the Email tone", change_email_tone)
emailtone_graph.add_edge(START, "Change the Email tone")
emailtone_graph.add_edge("Change the Email tone", END)

graph = emailtone_graph.compile()