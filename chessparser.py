"""doc"""

import chess.pgn
import sqlite3
from sqlite3 import IntegrityError

PGN_FILE = "ficsgamesdb_201701_standard2000_nomovetimes_1465638.pgn"
DB_PATH = "chess.sqlite"

def fetch_game_data(game):
    eco_code = game.headers["ECO"]
    time, increment = game.headers["TimeControl"].split("+")
    result = game.headers["Result"]
    year, month, _ = game.headers["Date"].split(".")
    white_elo = game.headers["WhiteElo"]
    black_elo = game.headers["BlackElo"]
    gameid = "FICS" + game.headers["FICSGamesDBGameNo"]
    return result, year, month, white_elo, black_elo, eco_code, time, increment, gameid

def add_games_to_db(inputfile, outputfile):
    """doc"""
    conn = sqlite3.connect(outputfile)
    c = conn.cursor()
    with open(inputfile) as pgn:
        curr_game = chess.pgn.read_game(pgn)
        counter = 0
        while curr_game != None and counter < 100:
            result, year, month, white_elo, black_elo, eco_code, time, increment, gameid = fetch_game_data(curr_game)
            try:
                c.execute("""INSERT INTO Eco(code)
                            VALUES (?)""", (eco_code,))
                c.execute("""INSERT INTO TimeControl(time, increment)
                            VALUES (?,?)""", (time, increment,))
            except IntegrityError:
                pass
            c.execute("""INSERT INTO Games
                        VALUES (?,?,?,?,?,?,?,?,?)""", (result, year, month, white_elo, black_elo, eco_code, time, increment, gameid,))
            counter += 1
            if counter % 10 == 0:
                print(counter)
            curr_game = chess.pgn.read_game(pgn)
    conn.commit()
    conn.close()

def main():
    """doc"""
    add_games_to_db(PGN_FILE, DB_PATH)

if __name__ == "__main__":
    main()
