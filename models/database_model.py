import sqlite3
import os

class DatabaseModel:
    def __init__(self):
        self.db_path = ':memory:'
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY, name TEXT, email TEXT, role TEXT)''')
        cursor.execute("INSERT INTO users VALUES (1, 'Alice', 'alice@example.com', 'user')")
        cursor.execute("INSERT INTO users VALUES (2, 'Bob', 'bob@example.com', 'admin')")
        cursor.execute("INSERT INTO users VALUES (3, 'Charlie', 'charlie@example.com', 'user')")
        self.conn.commit()

    def execute_query(self, query):
        cursor = self.conn.cursor()
        sql = f"SELECT * FROM users WHERE name LIKE '%{query}%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return {'results': results}

    def execute_complex_query(self, query_data):
        cursor = self.conn.cursor()
        cursor.execute(query_data['sql'])
        results = cursor.fetchall()
        return {'results': results}
