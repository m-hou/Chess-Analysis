"""doc"""

### SETTINGS ###

# CHARTS TO AGGREGATE
CHART_1 = True  # SQL
CHART_2 = True  # SQL
CHART_3 = True  # Neo4j
CHART_4 = True  # Neo4j
CHART_5 = True  # Neo4j

# CHART 1
MIN_ELO = 0
MAX_ELO = 3000
INCREMENT = 25
LIMIT_OF_OPENINGS = 20

# CHART 3
PLY_LIMIT = 200

# CHART 5
GAMEID = "410983950"

### PATHS ###

# SOURCES
SQL_PGN_FILE = "pgnfiles/ficsgamesdb_2016_chess_nomovetimes_1482742.pgn"  # 12309953 games 2016
SQL_DB_PATH = "chess.sqlite"
NEO4J_PGN_FILE = "pgnfiles/output.pgn"  # 34382 games 2017 Jan >2000 Elo
NEO4J_DB_PATH = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASS = "pass"
NEO4J_GAME_INSERTS_PER_SESSION = 1000

# OUTPUT
DATA_OUTPUT_PATH = "assets/data/"
