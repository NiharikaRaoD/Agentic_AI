"""Simple LangGraph example demonstrating START, END, and StateGraph usage."""

from langgraph.graph import START, END, StateGraph
from typing import TypedDict

class MyState(TypedDict):
    """Defines the state structure shared across the LangGraph nodes.

    Attributes:
        name (str): The user's name or identifier.
        message (str): The generated greeting message.
    """
    name: str
    message: str

def say_hello(state: MyState) -> MyState:
    """ Node that generates a greeting message from the given name.

    This function represents a LangGraph node. Each node takes the
    current state as input, performs an operation, and returns the
    updated state.

    Args:
        state (MyState): The input state containing the user's name.

    Returns:
        MyState: The updated state containing the generated message.
    """

    state['message'] = f"Hello {state['name']}"
    return state

# Build the Langgraph workflow
state_graph = StateGraph(MyState)
state_graph.add_node("wish", say_hello)
state_graph.add_edge(START, "wish")
state_graph.add_edge("wish", END)

# Compile the executable graph
graph = state_graph.compile()

if __name__ == "__main__":
    # Example run
    output = graph.invoke({"name": "Sai"})
    print(output)