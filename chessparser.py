"""doc"""

import sqlite3
from sqlite3 import IntegrityError
import pgn

PGN_FILE = "ficsgamesdb_201701_standard2000_nomovetimes_1465638.pgn"
DB_PATH = "chess.sqlite"

def add_games_to_db(inputfile, outputfile):
    """doc"""
    conn = sqlite3.connect(outputfile)
    c = conn.cursor()
    games_parsed = 0
    for index, game in enumerate(pgn.GameIterator(inputfile)):
        e = (game.eco,)
        time, increment = game.timecontrol.split("+")
        t = (time, increment,)
        year, month, _ = game.date.split(".")
        g = (game.result, year, month, game.whiteelo, game.blackelo, game.eco, time, increment, game.ficsgamesdbgameno,)
        try:
            c.execute("""INSERT INTO Eco(code)
                        VALUES (?)""", e)
        except IntegrityError:
            pass
        try:
            c.execute("""INSERT INTO TimeControl(time, increment)
                        VALUES (?,?)""", t)
        except IntegrityError:
            pass
        c.execute("""INSERT INTO Games
                    VALUES (?,?,?,?,?,?,?,?,?)""", g)
        games_parsed = index + 1
        if games_parsed % 100 == 0:
            print(games_parsed)
    print(str(games_parsed) + " games parsed")
    conn.commit()
    conn.close()

def main():
    """doc"""
    add_games_to_db(PGN_FILE, DB_PATH)

if __name__ == "__main__":
    main()
