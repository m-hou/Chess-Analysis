### SETTINGS ###

# CHART 1
MIN_ELO = 0
MAX_ELO = 3000
INCREMENT = 25

### PATHS ###

# SOURCES
SQL_PGN_FILE = "pgnfiles/ficsgamesdb_2016_chess_nomovetimes_1482742.pgn" # 12309953 games 2016
SQL_DB_PATH = "chess.sqlite"
NEO4J_PGN_FILE = "pgnfiles/output.pgn" # 34382 games 2017 Jan >2000 Elo
NEO4J_DB_PATH = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASS = "pass"

# OUTPUT
DATA_OUTPUT_PATH = "assets/data/"
