from typing import TypedDict
from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import START, END, StateGraph

class History(TypedDict):
    Date: str
    History_Event: str

load_dotenv()
model_name = os.getenv('MODEL_NAME')
model_provider = os.getenv('MODEL_PROVIDER')
llm = init_chat_model(model=model_name, model_provider=model_provider)

def history_event(state:History) -> History:
    Date = state['Date'] 
    prompt = ChatPromptTemplate([
        ('system', 'You are an expert historian and good with dates'),
        ("user", "for the given {Date}"),
        ("user", "list out atleast 10 historic events which occured on that day")
    ])

    chain = prompt | llm 
    response = chain.invoke({'Date': Date})
    state['History_Event'] = response.content
    return state

history_graph = StateGraph(History)
history_graph.add_node("Historic Events", history_event)
history_graph.add_edge(START, "Historic Events" )
history_graph.add_edge("Historic Events", END)

graph = history_graph.compile()


