"""doc"""

import chess.pgn
from neo4j.v1 import GraphDatabase, basic_auth

PGN_FILE = "ficsgamesdb_201701_standard2000_nomovetimes_1465638.pgn"
DB_PATH = "bolt://localhost:7687"

def parse_first_game():
    """doc"""
    pgn = open(PGN_FILE)
    first_game = chess.pgn.read_game(pgn)
    pgn.close()

    node = first_game
    fens = []
    moves = []
    while not node.is_end():
        next_node = node.variation(0)
        fens.append(node.board().board_fen() + (" b", " w")[node.board().turn])
        moves.append(node.board().san(next_node.move))
        node = next_node
    fens.append(node.board().board_fen() + (" b", " w")[node.board().turn])
    return fens, moves

def neo4j():
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "neo4j"))
    session = driver.session()
    fens, moves = parse_first_game()
    print(len(fens), len(moves))
    print(moves)
    for i, _ in enumerate(moves):
        print(i)
        session.run(
            "MERGE (curr:Position {fen: {currFen}})"
            "MERGE (curr) -[:Move {move: {move}}]-> (:Position {fen: {nextFen}})",
            {"currFen": fens[i], "nextFen": fens[i+1], "move": moves[i]}
        )
    session.close()

def main():
    """doc"""
    neo4j()

if __name__ == "__main__":
    main()
