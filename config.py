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

# CHART 5
HARDCODED_FENS = [  # FICSID: 410983950
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -",
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3",
    "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6",
    "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq -",
    "r1bqkbnr/pp1ppppp/2n5/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -",
    "r1bqkbnr/pp1ppppp/2n5/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3",
    "r1bqkbnr/pp1ppppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq -",
    "r1bqkbnr/pp1ppppp/2n5/8/3NP3/8/PPP2PPP/RNBQKB1R b KQkq -",
    "r1bqkbnr/pp1p1ppp/2n5/4p3/3NP3/8/PPP2PPP/RNBQKB1R w KQkq e6",
    "r1bqkbnr/pp1p1ppp/2N5/4p3/4P3/8/PPP2PPP/RNBQKB1R b KQkq -",
    "r1bqkbnr/pp3ppp/2p5/4p3/4P3/8/PPP2PPP/RNBQKB1R w KQkq -",
    "r1bqkbnr/pp3ppp/2p5/4p3/4P3/3B4/PPP2PPP/RNBQK2R b KQkq -",
    "r1bqkb1r/pp3ppp/2p2n2/4p3/4P3/3B4/PPP2PPP/RNBQK2R w KQkq -",
    "r1bqkb1r/pp3ppp/2p2n2/4p3/4P3/3B4/PPP2PPP/RNBQ1RK1 b kq -",
    "r2qkb1r/pp3ppp/2p2n2/4p3/4P1b1/3B4/PPP2PPP/RNBQ1RK1 w kq -",
    "r2qkb1r/pp3ppp/2p2n2/4p3/4P1b1/3B1P2/PPP3PP/RNBQ1RK1 b kq -",
    "r2qk2r/pp3ppp/2p2n2/2b1p3/4P1b1/3B1P2/PPP3PP/RNBQ1RK1 w kq -",
    "r2qk2r/pp3ppp/2p2n2/2b1p3/4P1b1/3B1P2/PPP3PP/RNBQ1R1K b kq -",
    "r2qk2r/pp3ppp/2p1bn2/2b1p3/4P3/3B1P2/PPP3PP/RNBQ1R1K w kq -",
    "r2qk2r/pp3ppp/2p1bn2/2b1p3/4P3/2NB1P2/PPP3PP/R1BQ1R1K b kq -",
    "r2q1rk1/pp3ppp/2p1bn2/2b1p3/4P3/2NB1P2/PPP3PP/R1BQ1R1K w - -",
    "r2q1rk1/pp3ppp/2p1bn2/2b1p3/4P3/P1NB1P2/1PP3PP/R1BQ1R1K b - -",
    "r2q1rk1/pp3ppp/2p1b3/2b1p2n/4P3/P1NB1P2/1PP3PP/R1BQ1R1K w - -",
    "r2q1rk1/pp3ppp/2p1b3/2b1p2n/1P2P3/P1NB1P2/2P3PP/R1BQ1R1K b - b3",
    "r2q1rk1/pp3ppp/2p1b3/4p2n/1P1bP3/P1NB1P2/2P3PP/R1BQ1R1K w - -",
    "r2q1rk1/pp3ppp/2p1b3/4p2n/1P1bP3/P1NB1P2/1BP3PP/R2Q1R1K b - -",
    "r2q1rk1/pp3ppp/2p1b3/4p3/1P1bP3/P1NB1Pn1/1BP3PP/R2Q1R1K w - -",
    "r2q1rk1/pp3ppp/2p1b3/4p3/1P1bP3/P1NB1PP1/1BP3P1/R2Q1R1K b - -",
    "r4rk1/pp3ppp/2p1b3/4p1q1/1P1bP3/P1NB1PP1/1BP3P1/R2Q1R1K w - -",
    "r4rk1/pp3ppp/2p1b3/4p1q1/1P1bPP2/P1NB2P1/1BP3P1/R2Q1R1K b - -",
    "r4rk1/pp3ppp/2p1b2q/4p3/1P1bPP2/P1NB2P1/1BP3P1/R2Q1R1K w - -",
    "r4rk1/pp3ppp/2p1b2q/4p2Q/1P1bPP2/P1NB2P1/1BP3P1/R4R1K b - -",
    "r4rk1/pp3ppp/2p1b3/4p2q/1P1bPP2/P1NB2P1/1BP3P1/R4R1K w - -"
]

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
