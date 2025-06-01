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
    Subject: Request for Quote for Solar Panels

Dear John,

I hope you are doing well.

I am reaching out to request a quotation for solar panels. We are looking to purchase solar panels for a rooftop installation and would like to know the pricing and specifications for the following:

Solar panel capacity:  550W each

Quantity: 10 panels

Delivery location: Capetown

Any warranties or after-sales support included


Looking forward to your quote.

Best regards,
Vetori
    """
    run(sample_email)
