from utils.ollama_clients import query_ollama
from memory.shared_memory import log_to_memory
import json

def email_agent(state: dict) -> dict:
    text = state["input"]
    prompt = f"""Extract key info from this email:
---
{text}
---
Respond in JSON with sender, urgency, and message_summary."""
    result = query_ollama(prompt)

    # Save to memory
    print(state['intent'])
    print(result)
    parsed_result = json.loads(result)
    log_to_memory(source="email", file_type="Email", intent=state["intent"], extracted_data=parsed_result)

    state["output"] = result
    return state
