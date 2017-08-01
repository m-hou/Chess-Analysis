"""doc"""

### SETTINGS ###

# CHARTS TO AGGREGATE
CHART_1 = True # SQL
CHART_2 = True # SQL
CHART_3 = True # Neo4j
CHART_4 = True # Neo4j
CHART_5 = True # Neo4j
 
# CHART 1
MIN_ELO = 0
MAX_ELO = 3000
INCREMENT = 25

# CHART 5
HARDCODED_FENS = [ #FICSID: 410988434
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -",
    "rnbqkbnr/pppppppp/8/8/8/6P1/PPPPPP1P/RNBQKBNR b KQkq -",
    "rnbqkbnr/pppp1ppp/8/4p3/8/6P1/PPPPPP1P/RNBQKBNR w KQkq e6",
    "rnbqkbnr/pppp1ppp/8/4p3/8/6P1/PPPPPPBP/RNBQK1NR b KQkq -",
    "rnbqkb1r/pppp1ppp/5n2/4p3/8/6P1/PPPPPPBP/RNBQK1NR w KQkq -",
    "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/6P1/PPPP1PBP/RNBQK1NR b KQkq e3",
    "rnbq1b1r/ppppkppp/5n2/4p3/4P3/6P1/PPPP1PBP/RNBQK1NR w KQ -",
    "rnbq1b1r/ppppkppp/5n2/4p3/3PP3/6P1/PPP2PBP/RNBQK1NR b KQ d3",
    "rnbq1b1r/ppp1kppp/3p1n2/4p3/3PP3/6P1/PPP2PBP/RNBQK1NR w KQ -",
    "rnbq1b1r/ppp1kppp/3p1n2/4p3/3PP3/5NP1/PPP2PBP/RNBQK2R b KQ -",
    "rnbq1b1r/ppp1kpp1/3p1n1p/4p3/3PP3/5NP1/PPP2PBP/RNBQK2R w KQ -",
    "rnbq1b1r/ppp1kpp1/3p1n1p/4p3/3PP3/5NP1/PPP2PBP/RNBQ1RK1 b - -",
    "r1bq1b1r/pppnkpp1/3p1n1p/4p3/3PP3/5NP1/PPP2PBP/RNBQ1RK1 w - -",
    "r1bq1b1r/pppnkpp1/3p1n1p/4p3/3PP3/5NP1/PPP1QPBP/RNB2RK1 b - -",
    "r1bq1b1r/pppnkp2/3p1npp/4p3/3PP3/5NP1/PPP1QPBP/RNB2RK1 w - -",
    "r1bq1b1r/pppnkp2/3p1npp/4p3/3PP3/5NP1/PPP1QPBP/RNBR2K1 b - -",
    "r1bq1b1r/pppnkp2/3p1npp/8/3pP3/5NP1/PPP1QPBP/RNBR2K1 w - -",
    "r1bq1b1r/pppnkp2/3p1npp/4P3/3p4/5NP1/PPP1QPBP/RNBR2K1 b - -",
    "r1bq1b1r/pppnkp2/5npp/4p3/3p4/5NP1/PPP1QPBP/RNBR2K1 w - -",
    "r1bq1b1r/pppnkp2/5npp/4N3/3p4/6P1/PPP1QPBP/RNBR2K1 b - -",
    "r1bq1b1r/ppp1kp2/5npp/4n3/3p4/6P1/PPP1QPBP/RNBR2K1 w - -",
    "r1bq1b1r/ppp1kp2/5npp/4Q3/3p4/6P1/PPP2PBP/RNBR2K1 b - -",
    "r2q1b1r/ppp1kp2/4bnpp/4Q3/3p4/6P1/PPP2PBP/RNBR2K1 w - -",
    "r2q1b1r/pBp1kp2/4bnpp/4Q3/3p4/6P1/PPP2P1P/RNBR2K1 b - -",
    "1r1q1b1r/pBp1kp2/4bnpp/4Q3/3p4/6P1/PPP2P1P/RNBR2K1 w - -",
    "1r1q1b1r/pBp1kp2/4bnpp/4Q3/3R4/6P1/PPP2P1P/RNB3K1 b - -",
    "1r2qb1r/pBp1kp2/4bnpp/4Q3/3R4/6P1/PPP2P1P/RNB3K1 w - -",
    "1r2qb1r/pBp1kp2/4bnpp/2Q5/3R4/6P1/PPP2P1P/RNB3K1 b - -",
]

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
