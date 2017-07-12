"""doc"""

import sys
import chess.pgn
from neo4j.v1 import GraphDatabase, basic_auth

PGN_FILE = "fics_201701_standard2000_fen.pgn"
DB_PATH = "bolt://localhost:7687"

def remove_extra_fen_info(fen):
    """doc"""
    return " ".join(fen.split(" ")[:-3])

def parse_games(amount):
    """doc"""
    with open(PGN_FILE) as pgn:
        first_game = chess.pgn.read_game(pgn)
        counter = 0
        while first_game != None and counter < amount:
            game = first_game
            fens = [remove_extra_fen_info(chess.STARTING_FEN)]
            moves = []
            while not game.is_end():
                next_node = game.variation(0)
                fens.append(remove_extra_fen_info(next_node.comment))
                moves.append(game.board().san(next_node.move))
                game = next_node
            first_game = chess.pgn.read_game(pgn)
            counter += 1
            print(counter)
            yield fens, moves, first_game

def insert(amount=sys.maxsize):
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "pass"))
    session = driver.session()
    for fens, moves, game in parse_games(amount):
        for i, _ in enumerate(moves):
            if i == len(moves) - 1:
                session.run(
                    "MERGE (curr:Position {fen: {currFen}})"
                    "MERGE (next:Position {fen: {nextFen}})"
                    "MERGE (curr) -[:Move {move: {move}}]-> (next)"
                    "MERGE (game:Game {elo: {elo}, timeControl: {timeControl}, result: {result}, ficsid: {ficsid}})"
                    "MERGE (next) -[:PlayedIn]-> (game)",
                    {"currFen": fens[i], "nextFen": fens[i+1], "move": moves[i],
                     "elo": (int(game.headers["WhiteElo"]) + int(game.headers["BlackElo"])) / 2,
                     "timeControl": game.headers["TimeControl"], "result": game.headers["Result"],
                     "ficsid": game.headers["FICSGamesDBGameNo"]}
                )
            else:
                session.run(
                    "MERGE (curr:Position {fen: {currFen}})"
                    "MERGE (next:Position {fen: {nextFen}})"
                    "MERGE (curr) -[:Move {move: {move}}]-> (next)"
                    "MERGE (game:Game {elo: {elo}, timeControl: {timeControl}, result: {result}, ficsid: {ficsid}})",
                    {"currFen": fens[i], "nextFen": fens[i+1], "move": moves[i],
                     "elo": (int(game.headers["WhiteElo"]) + int(game.headers["BlackElo"])) / 2,
                     "timeControl": game.headers["TimeControl"], "result": game.headers["Result"],
                     "ficsid": game.headers["FICSGamesDBGameNo"]}
                )
    session.close()

def main():
    """doc"""
    insert()

if __name__ == "__main__":
    main()
