"""doc"""

import chess.pgn
from neo4j.v1 import GraphDatabase, basic_auth

PGN_FILE = "ficsgamesdb_201701_standard2000_nomovetimes_1465638.pgn"
DB_PATH = "bolt://localhost:7687"

def fen():
    """doc"""
    pgn = open(PGN_FILE)
    first_game = chess.pgn.read_game(pgn)
    pgn.close()

    node = first_game
    while not node.is_end():
        next_node = node.variation(0)
        print(node.board().fen())
        node = next_node

def main():
    """doc"""
    #fen()
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "neo4j"))
    session = driver.session()

    session.run("CREATE (a:Person {name: {name}, title: {title}})",
                {"name": "Arthur", "title": "King"})

    result = session.run("MATCH (a:Person) WHERE a.name = {name} "
                         "RETURN a.name AS name, a.title AS title",
                         {"name": "Arthur"})
    for record in result:
        print("%s %s" % (record["title"], record["name"]))

    session.close()

if __name__ == "__main__":
    main()
