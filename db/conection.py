import sqlite3
def get_connection():
    conn = sqlite3.connect(db_connection)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


db_connection = "C:\Users\משתמש\Desktop\sivata_project\my.db"