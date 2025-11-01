from langgraph.graph import START, END, StateGraph
from typing import TypedDict

class Input(TypedDict):
    a: int
    b: int
    result: int|None

def sum(state: Input) -> Input:
    a = state['a']
    b = state['b']
    state['result'] = a + b
    return state

# Build the Langgraph workflow
state_graph = StateGraph(Input)
state_graph.add_node("Add", sum)
state_graph.add_edge(START, "Add")
state_graph.add_edge("Add", END)

# Compile the executable graph
graph = state_graph.compile()

