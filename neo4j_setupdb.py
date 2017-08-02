"""doc"""

from neo4j.v1 import GraphDatabase, basic_auth
import config

def query_db():
    """doc"""
    driver = GraphDatabase.driver(config.NEO4J_DB_PATH, auth=basic_auth(config.NEO4J_USER, config.NEO4J_PASS))
    with driver.session() as session:
        session.run("CREATE INDEX ON :Game(gameid)")
        session.run("CREATE INDEX ON :Position(fen)")
        session.run("CREATE INDEX ON :Ply(moveNumber)")

def main():
    """doc"""
    query_db()

if __name__ == "__main__":
    main()
