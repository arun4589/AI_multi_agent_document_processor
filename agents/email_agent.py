from utils.ollama_clients import query_ollama
from memory.shared_memory import log_to_memory
import json

def email_agent(state: dict) -> dict:
    text = state["input"]
    prompt = f"""Extract key info from this email:
---
{text}
---
Respond strictly means strictly in JSON with  intent ,sender, urgency, and message_summary."""
    result = query_ollama(prompt)

    # Save to memory
    print(state['intent'])
    # print('hi')
    # print(result)
    # parsed_result = json.loads(result)
    try:
       log_to_memory(source="email", file_type="Email", intent=state["intent"], extracted_data=result)
    except Exception as e:
       print("DB Error:", e)

    state["output"] = result
    return state
