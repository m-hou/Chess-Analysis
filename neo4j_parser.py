"""doc"""

import sys
import pgn
from neo4j.v1 import GraphDatabase, basic_auth

NUMBER_OF_COMMENTS = 1
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"
PGN_FILE = "pgnfiles/output.pgn"
DB_PATH = "bolt://localhost:7687"

def parse_fen(comment):
    return " ".join(comment[2:-2].split(" ")[:-4])

def get_fens(game):
    return [STARTING_FEN] + [parse_fen(fen) for fen in game.moves[1:-1:NUMBER_OF_COMMENTS + 1]]

def get_moves(game):
    return game.moves[:-1:NUMBER_OF_COMMENTS + 1]

def insert(amount=sys.maxsize):
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "pass"))
    session = driver.session()
    for count, game in enumerate(pgn.GameIterator(PGN_FILE)):
        gameid = "FICS" + game.ficsgamesdbgameno
        result = game.result
        fens = get_fens(game)
        moves = get_moves(game)
        print(count)
        for index, _ in enumerate(moves):
            args = {"currFen": fens[index], "nextFen": fens[index+1], "move": moves[index],
                    "result": result, "gameid": gameid}
            if index == len(moves) - 1:
                session.run(
                    "MERGE (curr:Position {fen: {currFen}})"
                    "MERGE (next:Position {fen: {nextFen}})"
                    "MERGE (curr) -[:Move {move: {move}}]-> (next)"
                    "MERGE (game:Game {result: {result}, gameid: {gameid}})"
                    "MERGE (next) -[:PlayedIn]-> (game)", args)
            else:
                session.run(
                    "MERGE (curr:Position {fen: {currFen}})"
                    "MERGE (next:Position {fen: {nextFen}})"
                    "MERGE (curr) -[:Move {move: {move}}]-> (next)"
                    "MERGE (game:Game {result: {result}, gameid: {gameid}})", args)
    session.close()

def main():
    """doc"""
    insert()

if __name__ == "__main__":
    main()
