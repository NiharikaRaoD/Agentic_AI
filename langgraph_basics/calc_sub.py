from langgraph.graph import START, END, StateGraph
from typing import TypedDict

class Input(TypedDict):
    a: int
    b: int
    result: int|None

def difference(state: Input) -> Input:
    a = state['a']
    b = state['b']
    state['result'] = a - b
    return state

# Build the Langgraph workflow
state_graph = StateGraph(Input)
state_graph.add_node("Subtract", difference)
state_graph.add_edge(START, "Subtract")
state_graph.add_edge("Subtract", END)

# Compile the executable graph
graph = state_graph.compile()