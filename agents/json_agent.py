from utils.ollama_clients import query_ollama
from memory.shared_memory import log_to_memory

def json_agent(state: dict) -> dict:
    text = state["input"]
    prompt = f"""Process this JSON and reformat it to a target schema. Flag missing fields:
---
{text}
---
Respond in JSON."""
    result = query_ollama(prompt)

    # Save to memory
    log_to_memory(source="json", file_type="JSON", intent=state["intent"], extracted_data=result)

    state["output"] = result
    return state
