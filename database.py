
import sqlite3

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            fixed_expense BOOLEAN NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(db_path, date, type_, amount, category, description, fixed_expense):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO transactions (date, type, amount, category, description, fixed_expense) VALUES (?, ?, ?, ?, ?, ?)",
              (date, type_, amount, category, description, fixed_expense))
    conn.commit()
    conn.close()

def get_transactions(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    conn.close()
    return transactions
