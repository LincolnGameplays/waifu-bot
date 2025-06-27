import sqlite3
import json
from datetime import datetime

def init_db():
    conn = sqlite3.connect('kaoruko_memories.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (user_id INTEGER PRIMARY KEY, 
                  name TEXT, 
                  preferred_language TEXT,
                  affection_level REAL DEFAULT 1.0)''')
                  
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  user_message TEXT,
                  bot_response TEXT,
                  emotion TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    
    conn.commit()
    return conn

def save_conversation(user_id, user_msg, bot_response, emotion):
    conn = init_db()
    c = conn.cursor()
    
    # Verificar se usuário existe
    c.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
    if not c.fetchone():
        c.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
    
    # Salvar conversa
    c.execute('''INSERT INTO conversations 
                 (user_id, user_message, bot_response, emotion) 
                 VALUES (?, ?, ?, ?)''',
                 (user_id, user_msg, bot_response, emotion))
    
    # Aumentar afeto
    if emotion in ["love", "happy"]:
        c.execute("UPDATE users SET affection_level = affection_level + 0.1 WHERE user_id = ?", (user_id,))
    
    conn.commit()
    conn.close()
