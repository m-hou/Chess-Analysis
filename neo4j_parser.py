"""doc"""

import sys
import pgn
from neo4j.v1 import GraphDatabase, basic_auth

NUMBER_OF_COMMENTS = 2
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"
STARTING_EVAL = 0.0
PGN_FILE = "pgnfiles/output.pgn"
DB_PATH = "bolt://localhost:7687"

def parse_move(move):
    return move

def parse_fen(comment):
    return " ".join(comment[2:-2].split(" ")[:-3])

def parse_eval(comment):
    return comment[2:-2]

def parse_move_comments(game):
    partitions = NUMBER_OF_COMMENTS + 1
    return [game.moves[i:-1:partitions] for i in range(partitions)]


def insert(amount=sys.maxsize):
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "pass"))
    session = driver.session()
    for count, game in enumerate(pgn.GameIterator(PGN_FILE)):
        gameid = "FICS" + game.ficsgamesdbgameno
        result = game.result
        moves, evals, fens = parse_move_comments(game)
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
