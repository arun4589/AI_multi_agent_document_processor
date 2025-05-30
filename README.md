#  Multi-Agent AI Document Processor

##  Objective

Build a multi-agent AI system that:
- Accepts input in **PDF**, **JSON**, or **Email (text)** formats.
- **Classifies** the format and **detects intent**.
- **Routes** the input to the correct agent for processing.
- **Extracts relevant data** and **logs context** in a shared SQLite memory.

---

##  Features

- **Classifier Agent**: Identifies input format and intent.
- **JSON Agent**: Validates and extracts structured data from JSON, flags anomalies.
- **Email Agent**: Extracts sender info, urgency, and CRM-friendly summary.
- **Shared Memory**: Stores format, intent, timestamps, and extracted data using SQLite.
- Built with **LangGraph**, powered by **Ollama LLM** (running locally).

---


---

##  Agents Description

### 1. Classifier Agent
- **Input**: Raw text or file contents.
- **Output**: Format (`PDF`, `JSON`, `Email`) and Intent (`RFQ`, `Invoice`, `Complaint`, etc.)
- **Routing**: Forwards to the appropriate downstream agent.

### 2. JSON Agent
- **Input**: JSON payload.
- **Tasks**:
  - Validate against a target schema.
  - Extract key fields.
  - Detect and flag missing or invalid fields.

### 3. Email Agent
- **Input**: Email text.
- **Tasks**:
  - Extract `sender`, `urgency`, and `message_summary`.
  - Return data in CRM-ready structure.

---

##  Shared Memory (SQLite)

SQLite is used to:
- Track processed inputs.
- Store `source`, `file_type`, `intent`, `timestamp`, `thread_id`, and `extracted_data`.
- Enable traceability and chaining between steps.

## Folder structure 

flowbit/
│
├── agents/
│   ├── classifier.py
│   ├── email_agent.py
│   └── json_agent.py
│
├── memory/
│   └── shared_memory.py
│
├── utils/
│   └── ollama_clients.py
├── graph/
│   └── multi_agent_graph.py
│
│
├── output_screenshots/email/json
├── output.py
├── main.py
├── requirements.txt
└── README.md


## Setup

### Clone the repo
```bash
git clone <your-repo-url>
cd flowbit
```

### Create virtual Environment
```bash
python -m venv flowbit
flowbit\Scripts\activate  
```
### Install requirements
```bash
pip install -r requirements.txt
```

### RUN 
```bash
python main.py
```


