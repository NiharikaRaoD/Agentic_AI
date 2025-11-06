from typing import TypedDict, Literal
from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import START, END, StateGraph

class MathAgent(TypedDict):
    query: str
    explanation: bool
    result: str

load_dotenv()
model_name = os.getenv('MODEL_NAME')
model_provider = os.getenv('MODEL_PROVIDER')
llm = init_chat_model(model=model_name, model_provider=model_provider)

def give_me_result(state:MathAgent) -> MathAgent:
    query = state['query']
    prompt = f"You are an expert in Mathematics. Give me the result of the given math problem {query}. No explanation required"
    state['result'] = llm.invoke(prompt)
    return state

def give_me_explanation(state:MathAgent) -> MathAgent:
    explanation = state['explanation']
    prompt = f"You are an expert in Mathematics. Give me the step to step explanation on how to solve the given math problem {explanation}. "
    state['result'] = llm.invoke(prompt)
    return state

def next_node(state) -> Literal['Respond', 'Explain']:
    if state['explanation'] == True:
        return 'Explain'
    return 'Respond'


math_agent_graph = StateGraph(MathAgent)
math_agent_graph.add_node("Respond", give_me_result)
math_agent_graph.add_node("Explain", give_me_explanation)
math_agent_graph.add_conditional_edges(START, next_node)
math_agent_graph.add_edge("Respond", END)
math_agent_graph.add_edge("Explain", END)

graph = math_agent_graph.compile()
