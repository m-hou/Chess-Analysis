"""doc"""

import chess.pgn

PGN_FILE = "ficsgamesdb_201701_standard2000_nomovetimes_1465638.pgn"

def main():
    """doc"""
    pgn = open(PGN_FILE)
    first_game = chess.pgn.read_game(pgn)
    pgn.close()

    node = first_game
    while not node.is_end():
        next_node = node.variation(0)
        print(node.board().fen())
        node = next_node

if __name__ == "__main__":
    main()
