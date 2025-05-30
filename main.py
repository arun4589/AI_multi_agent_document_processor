from graph.multi_agent_graph import build_graph
from memory.shared_memory import init_db

def run(input_text):
    init_db()
    graph = build_graph()
    initial_state = {"input": input_text}
    result = graph.invoke(initial_state)
    print("Final Output:\n", result)

if __name__ == "__main__":
    sample_json="""{
    "invoice_id": "INV-12345",
    "date": "2025-05-30",
    "customer": {
    "name": "ABC Corp",
    "email": "contact@abccorp.com"
    
    },
    "items": [
    {
      "description": "Solar Panel 300W",
      "quantity": 10
      
    },
    {
      
      "quantity": 5,
      "unit_price": 150.0
    }
    ],
  
    "currency": "USD"
    }
    """
    sample_email = """
    Subject: Urgent RFQ
    Hello team,
    Please send a quote for 500 units of solar panels.
    Regards,
    John
    """
    run(sample_email)
