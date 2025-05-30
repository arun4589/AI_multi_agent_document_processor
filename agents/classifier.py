from utils.ollama_clients import query_ollama
import json

def classifier_agent(state: dict) -> dict:
    text = state["input"]
    prompt = f"""Classify the following input:
---
{text}
---
Respond in JSON with "format" and "intent"."""
    result = query_ollama(prompt)
    result_json = json.loads(result)
    
    # Update state
    state.update({
        "format": result_json["format"],
        "intent": result_json["intent"]
    })
    return state
