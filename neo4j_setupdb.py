"""doc"""

from neo4j.v1 import GraphDatabase, basic_auth

DB_PATH = "bolt://localhost:7687"

def query_db():
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "pass"))
    session = driver.session()
    session.run("CREATE INDEX ON :Game(gameid)")
    session.run("CREATE INDEX ON :Position(fen)")
    session.run("CREATE INDEX ON :Ply(moveNumber)")
    session.close()

def main():
    """doc"""
    query_db()

if __name__ == "__main__":
    main()
