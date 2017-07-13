"""doc"""

from neo4j.v1 import GraphDatabase, basic_auth

DB_PATH = "bolt://localhost:7687"

def get_best_moves():
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "pass"))
    session = driver.session()
    result = session.run(
        """
        MATCH (:Position {fen: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"})-[m:Move]->(next:Position)
        MATCH (next)-[:Move*..1000]->()<-[:FinalPosition]-(g:Game) WITH DISTINCT g AS Games, m AS Moves
        RETURN Moves.move AS move, SUM(
            CASE Games.result
                WHEN '1-0' THEN 1
                WHEN '1/2-1/2' THEN 0.5
                WHEN '0-1' THEN 0
            END
        ) / count(Games) AS winrate, count(Games) AS freq""",
        {"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq"}
    )
    counter = 0
    for record in result:
        counter += 1
        print("%s %s %s" % (record["move"], record["winrate"], record["freq"]))
    print(counter)
    session.close()

def main():
    """doc"""
    get_best_moves()

if __name__ == "__main__":
    main()
