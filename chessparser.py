"""doc"""

import sqlite3
from sqlite3 import IntegrityError
import pgn

PGN_FILE = "ficsgamesdb_201701_chess_nomovetimes_1477065.pgn"
DB_PATH = "chess.sqlite"

def add_games_to_db(inputfile, outputfile):
    """doc"""
    conn = sqlite3.connect(outputfile)
    c = conn.cursor()
    games_inserted = 0
    for index, game in enumerate(pgn.GameIterator(inputfile)):
        e, t, g = parse_games(game)
        try:
            c.execute("""INSERT INTO TimeControl(time, increment)
                        VALUES (?,?)""", t)
        except IntegrityError:
            pass
        c.execute("""INSERT INTO Games
                    VALUES (?,?,?,?,?,?,?,?,?)""", g)
        games_inserted = index + 1
        if games_inserted % 100 == 0:
            print(games_inserted)
    print(str(games_inserted) + " games inserted")
    conn.commit()
    conn.close()

def parse_games(game):
    e = (game.eco,)
    time, increment = game.timecontrol.split("+")
    t = (time, increment,)
    year, month, _ = game.date.split(".")
    gameid = "FICS" + game.ficsgamesdbgameno
    g = (game.result, year, month, game.whiteelo, game.blackelo,
         game.eco, time, increment, gameid,)
    return e, t, g

def main():
    """doc"""
    add_games_to_db(PGN_FILE, DB_PATH)

if __name__ == "__main__":
    main()
