import sqlite3
from datetime import datetime
import json

def init_db():
    conn = sqlite3.connect("shared_memory.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            file_type TEXT,
            intent TEXT,
            timestamp TEXT,
            extracted_data TEXT,
            thread_id TEXT
        )
    ''')
    conn.commit()
    return conn

def log_to_memory(source, file_type, intent, extracted_data, thread_id=None):
    conn = sqlite3.connect("shared_memory.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO memory (source, file_type, intent, timestamp, extracted_data, thread_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (source, file_type, intent, datetime.now().isoformat(), json.dumps(extracted_data), thread_id))
    conn.commit()
    conn.close()
