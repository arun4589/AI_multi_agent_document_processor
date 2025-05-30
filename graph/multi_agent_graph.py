from langgraph.graph import StateGraph, END
from agents.classifier import classifier_agent
from agents.email_agent import email_agent
from agents.json_agent import json_agent
from typing import TypedDict, Optional, Any

class GraphState(TypedDict):
    input: str
    format: Optional[str]
    intent: Optional[str]
    output: Optional[dict]
    memory_id: Optional[int]

def router(state):
    if state["format"] == "Email":
        return "email_agent"
    elif state["format"] == "JSON":
        return "json_agent"
    else:
        return END

def build_graph():
    builder = StateGraph(GraphState)
    
    builder.add_node("classifier", classifier_agent)
    builder.add_node("email_agent", email_agent)
    builder.add_node("json_agent", json_agent)
    
    builder.set_entry_point("classifier")
    builder.add_conditional_edges("classifier", router, {
        "email_agent": "email_agent",
        "json_agent": "json_agent",
        END: END
    })

    builder.add_edge("email_agent", END)
    builder.add_edge("json_agent", END)

    return builder.compile()
