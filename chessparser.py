"""doc"""

import chess.pgn
import sqlite3

PGN_FILE = "ficsgamesdb_201701_standard2000_nomovetimes_1465638.pgn"
DB_PATH = "chess.sqlite"

def add_games_to_db(inputfile, outputfile, clear=False):
    """doc"""
    conn = sqlite3.connect(outputfile)
    c = conn.cursor()
    conn.commit()
    conn.close()

def main():
    """doc"""
    add_games_to_db(PGN_FILE, DB_PATH)

if __name__ == "__main__":
    main()
