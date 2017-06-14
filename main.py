"""doc"""

import sys
import chess.pgn
from neo4j.v1 import GraphDatabase, basic_auth

PGN_FILE = "ficsgamesdb_201701_standard2000_nomovetimes_1465638.pgn"
DB_PATH = "bolt://localhost:7687"

def parse_games_for_fast_query(amount):
    """doc"""
    with open(PGN_FILE) as pgn:
        first_game = chess.pgn.read_game(pgn)
        counter = 0
        while first_game != None and counter < amount:
            game = first_game
            fens = []
            moves = []
            while not game.is_end():
                next_node = game.variation(0)
                fens.append(game.board().board_fen() + (" b", " w")[game.board().turn])
                moves.append(game.board().san(next_node.move))
                game = next_node
            fens.append(game.board().board_fen() + (" b", " w")[game.board().turn])

            first_game = chess.pgn.read_game(pgn)
            counter += 1
            print(counter)
            yield fens, moves, first_game

def parse_games_for_space_efficiency(amount):
    """doc"""
    with open(PGN_FILE) as pgn:
        first_game = chess.pgn.read_game(pgn)
        counter = 0
        while first_game != None and counter < amount:
            game = first_game
            moves = []
            while not game.is_end():
                next_node = game.variation(0)
                moves.append(game.board().san(next_node.move))
                game = next_node

            first_game = chess.pgn.read_game(pgn)
            counter += 1
            print(counter)
            yield moves, first_game

def insert_for_fast_query(amount):
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "pass"))
    session = driver.session()
    for fens, moves, game in parse_games_for_fast_query(amount):
        for i, _ in enumerate(moves):
            session.run(
                "MERGE (curr:Position {fen: {currFen}})"
                "MERGE (curr) -[:Move {move: {move}}]-> (next:Position {fen: {nextFen}})"
                "CREATE (game:Game {elo: {elo}, timeControl: {timeControl}, result: {result}})"
                "MERGE (curr) -[:PlayedIn]-> (game)"
                "MERGE (next) -[:PlayedIn]-> (game)",
                {"currFen": fens[i], "nextFen": fens[i+1], "move": moves[i],
                 "elo": (int(game.headers["WhiteElo"]) + int(game.headers["BlackElo"])) / 2,
                 "timeControl": game.headers["TimeControl"], "result": game.headers["Result"]}
            )
    session.close()

def insert_for_space_efficiency(amount=sys.maxsize):
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "pass"))
    session = driver.session()
    for fens, moves, game in parse_games_for_space_efficiency(amount):
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
    #insert_for_fast_query(1000)
    insert_for_space_efficiency()

if __name__ == "__main__":
    main()
