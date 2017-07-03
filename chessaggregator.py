"""doc"""

import sqlite3

DB_PATH = "chess.sqlite"

def query_db(db_path):
    """doc"""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""""")
    conn.commit()
    conn.close()

def main():
    """doc"""
    query_db(DB_PATH)

if __name__ == "__main__":
    main()
