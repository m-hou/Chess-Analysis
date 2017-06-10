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

    game = first_game
    fens = []
    moves = []
    while not game.is_end():
        next_node = game.variation(0)
        fens.append(game.board().board_fen() + (" b", " w")[game.board().turn])
        moves.append(game.board().san(next_node.move))
        game = next_node
    fens.append(game.board().board_fen() + (" b", " w")[game.board().turn])
    return fens, moves, first_game

def neo4j():
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "neo4j"))
    session = driver.session()
    fens, moves, game = parse_first_game()
    print(len(fens), len(moves))
    print(moves)
    session.run("MATCH (n) DETACH DELETE n")
    for i, _ in enumerate(moves):
        print(i)
        session.run(
            "MERGE (curr:Position {fen: {currFen}})"
            "MERGE (curr) -[:Move {move: {move}}]-> (next:Position {fen: {nextFen}})"
            "MERGE (game:Game {elo: {elo}, timeControl: {timeControl}, result: {result}})"
            "MERGE (curr) -[:PlayedIn]-> (game)"
            "MERGE (next) -[:PlayedIn]-> (game)",
            {"currFen": fens[i], "nextFen": fens[i+1], "move": moves[i],
             "elo": (int(game.headers["WhiteElo"]) + int(game.headers["BlackElo"])) / 2,
             "timeControl": game.headers["TimeControl"], "result": game.headers["Result"]}
        )
    session.close()

def main():
    """doc"""
    neo4j()

if __name__ == "__main__":
    main()
