"""doc"""

import sys
import pgn
from neo4j.v1 import GraphDatabase, basic_auth
import config

NUMBER_OF_COMMENTS = 2
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -"
STARTING_EVAL = 0.0

def transform(sequence, index):
    """doc"""
    def transform_moves(moves):
        """doc"""
        return moves

    def transform_fens(fens):
        """doc"""
        return [STARTING_FEN] + [" ".join(fen[2:-2].split(" ")[:-2]) for fen in fens]

    def transform_evals(evals):
        """doc"""
        return [STARTING_EVAL] + [eval[2:-2] for eval in evals]

    transformations = [transform_moves, transform_evals, transform_fens]
    return transformations[index](sequence)

def parse_move_comments(game):
    """doc"""
    partitions = NUMBER_OF_COMMENTS + 1
    return [transform(game.moves[i:-1:partitions], i) for i in range(partitions)]

def parse_timecontrol(game):
    """doc"""
    for timecontrol in ["standard", "blitz", "lightning"]:
        if timecontrol in game.event:
            return timecontrol.capitalize()

def insert(amount=sys.maxsize):
    """doc"""
    driver = GraphDatabase.driver(config.NEO4J_DB_PATH, auth=basic_auth(config.NEO4J_USER, config.NEO4J_PASS))
    session = driver.session()
    for count, game in enumerate(pgn.GameIterator(config.NEO4J_PGN_FILE)):
        timecontrol = parse_timecontrol(game)
        gameid = "FICS" + game.ficsgamesdbgameno
        result = game.result
        moves, evals, fens = parse_move_comments(game)
        for index, _ in enumerate(moves):
            args = {"currFen": fens[index], "currEval": evals[index],
                    "nextFen": fens[index+1], "nextEval" :evals[index+1],
                    "move": moves[index], "result": result,
                    "gameid": gameid, "timecontrol": timecontrol,
                    "blackelo": game.blackelo, "whiteelo": game.whiteelo, "ply": index + 1}
            if index == len(moves) - 1:
                session.run(
                    """
                    MERGE (curr:Position {fen: {currFen}, eval: {currEval}})
                    MERGE (next:Position {fen: {nextFen}, eval: {nextEval}})
                    MERGE (curr) -[:Move {move: {move}}]-> (next)
                    MERGE (game:Game {result: {result}, gameid: {gameid},
                           whiteElo: {whiteelo}, blackElo: {blackelo}, timecontrol: {timecontrol}})
                    MERGE (game) -[:FinalPosition]-> (next)
                    MERGE (ply:Ply {moveNumber: {ply}})
                    MERGE (ply) -[:FinalPosition]-> (curr)""", args)
            else:
                session.run(
                    """
                    MERGE (curr:Position {fen: {currFen}, eval: {currEval}})
                    MERGE (next:Position {fen: {nextFen}, eval: {nextEval}})
                    MERGE (curr) -[:Move {move: {move}}]-> (next)
                    MERGE (game:Game {result: {result}, gameid: {gameid},
                           whiteElo: {whiteelo}, blackElo: {blackelo}, timecontrol: {timecontrol}})
                    MERGE (game) -[:HasPosition]-> (next)
                    MERGE (ply:Ply {moveNumber: {ply}})
                    MERGE (ply) -[:HasPosition]-> (curr)""", args)
        print(count + 1)
        if count + 1 >= amount:
            break
    session.close()

def main():
    """doc"""
    insert()

if __name__ == "__main__":
    main()
