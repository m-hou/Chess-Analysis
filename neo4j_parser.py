"""doc"""

import sys
import pgn
from neo4j.v1 import GraphDatabase, basic_auth

NUMBER_OF_COMMENTS = 2
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"
STARTING_EVAL = 0.0
PGN_FILE = "pgnfiles/output.pgn"
DB_PATH = "bolt://localhost:7687"

def transform(sequence, index):
    """doc"""
    def transform_moves(moves):
        """doc"""
        return moves

    def transform_fens(fens):
        """doc"""
        return [STARTING_FEN] + [" ".join(fen[2:-2].split(" ")[:-3]) for fen in fens]

    def transform_evals(evals):
        """doc"""
        return [STARTING_EVAL] + [eval[2:-2] for eval in evals]

    transformations = [transform_moves, transform_evals, transform_fens]
    return transformations[index](sequence)

def parse_move_comments(game):
    """doc"""
    partitions = NUMBER_OF_COMMENTS + 1
    return [transform(game.moves[i:-1:partitions], i) for i in range(partitions)]


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
