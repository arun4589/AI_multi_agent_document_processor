import sqlite3
import json

conn = sqlite3.connect("shared_memory.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM memory")
rows = cursor.fetchall()
for row in rows:
    print("ID:", row[0])
    print("Source:", row[1])
    print("Format:", row[2])
    print("Intent:", row[3])
    print("Timestamp:", row[4])
    print("Extracted Data:", json.loads(row[5]))  
    print("-" * 40)
   

conn.close()
