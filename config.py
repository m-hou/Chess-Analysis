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
LIMIT_OF_OPENINGS = 20

# CHART 5
HARDCODED_FENS = [  # FICSID: 410909817
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -",
    "rnbqkbnr/ppp1pppp/8/3p2B1/3P4/8/PPP1PPPP/RN1QKBNR b KQkq -",
    "r1bqkbnr/pppnpppp/8/3p2B1/3P4/8/PPP1PPPP/RN1QKBNR w KQkq -",
    "r1bqkbnr/pppnpppp/8/3p2B1/2PP4/8/PP2PPPP/RN1QKBNR b KQkq c3",
    "r1bqkbnr/pppnppp1/7p/3p2B1/2PP4/8/PP2PPPP/RN1QKBNR w KQkq -",
    "r1bqkbnr/pppnppp1/7p/3p4/2PP3B/8/PP2PPPP/RN1QKBNR b KQkq -",
    "r1bqkbnr/pppnppp1/7p/8/2pP3B/8/PP2PPPP/RN1QKBNR w KQkq -",
    "r1bqkbnr/pppnppp1/7p/8/2pP3B/4P3/PP3PPP/RN1QKBNR b KQkq -",
    "r1bqkbnr/p1pnppp1/7p/1p6/2pP3B/4P3/PP3PPP/RN1QKBNR w KQkq b6",
    "r1bqkbnr/p1pnppp1/7p/1p6/2pP3B/2N1P3/PP3PPP/R2QKBNR b KQkq -",
    "r1bqkbnr/p2nppp1/2p4p/1p6/2pP3B/2N1P3/PP3PPP/R2QKBNR w KQkq -",
    "r1bqkbnr/p2nppp1/2p4p/1p6/2pP3B/P1N1P3/1P3PPP/R2QKBNR b KQkq -",
    "r2qkbnr/pb1nppp1/2p4p/1p6/2pP3B/P1N1P3/1P3PPP/R2QKBNR w KQkq -",
    "r2qkbnr/pb1nppp1/2p4p/1p6/2pP3B/P1N1PN2/1P3PPP/R2QKB1R b KQkq -",
    "r2qkb1r/pb1nppp1/2p2n1p/1p6/2pP3B/P1N1PN2/1P3PPP/R2QKB1R w KQkq -",
    "r2qkb1r/pb1nppp1/2p2n1p/1p6/2pPP2B/P1N2N2/1P3PPP/R2QKB1R b KQkq -",
    "r2qkb1r/pb1n1pp1/2p1pn1p/1p6/2pPP2B/P1N2N2/1P3PPP/R2QKB1R w KQkq -",
    "r2qkb1r/pb1n1pp1/2p1pn1p/1p2P3/2pP3B/P1N2N2/1P3PPP/R2QKB1R b KQkq -",
    "r2qkb1r/pb1n1p2/2p1pn1p/1p2P1p1/2pP3B/P1N2N2/1P3PPP/R2QKB1R w KQkq g6",
    "r2qkb1r/pb1n1p2/2p1pn1p/1p2P1N1/2pP3B/P1N5/1P3PPP/R2QKB1R b KQkq -",
    "r2qkb1r/pb1n1p2/2p1pn2/1p2P1p1/2pP3B/P1N5/1P3PPP/R2QKB1R w KQkq -",
    "r2qkb1r/pb1n1p2/2p1pn2/1p2P1B1/2pP4/P1N5/1P3PPP/R2QKB1R b KQkq -",
    "r2qk2r/pb1nbp2/2p1pn2/1p2P1B1/2pP4/P1N5/1P3PPP/R2QKB1R w KQkq -",
    "r2qk2r/pb1nbp2/2p1pP2/1p4B1/2pP4/P1N5/1P3PPP/R2QKB1R b KQkq -",
    "r2qk2r/pb1n1p2/2p1pb2/1p4B1/2pP4/P1N5/1P3PPP/R2QKB1R w KQkq -",
    "r2qk2r/pb1n1p2/2p1pb2/1p6/2pP1B2/P1N5/1P3PPP/R2QKB1R b KQkq -",
    "r2qkn1r/pb3p2/2p1pb2/1p6/2pP1B2/P1N5/1P3PPP/R2QKB1R w KQkq -",
    "r2qkn1r/pb3p2/2p1pb2/1p6/2pP1B2/P1N5/1P2BPPP/R2QK2R b KQkq -",
    "r3kn1r/pb3p2/2p1pb2/1p6/2pq1B2/P1N5/1P2BPPP/R2QK2R w KQkq -",
    "r3kn1r/pb3p2/2p1pb2/1p6/2pq1B2/P1N5/1PQ1BPPP/R3K2R b KQkq -",
    "r3k2r/pb3p2/2p1pbn1/1p6/2pq1B2/P1N5/1PQ1BPPP/R3K2R w KQkq -",
    "r3k2r/pb3p2/2p1pbn1/1p6/2pq1B2/P1N5/1PQ1BPPP/3RK2R b Kkq -",
    "r3k2r/pb3p2/2p1pbn1/1p6/2p2q2/P1N5/1PQ1BPPP/3RK2R w Kkq -",
    "r3k2r/pb3p2/2p1pbn1/1p6/2p2q2/P1N2B2/1PQ2PPP/3RK2R b Kkq -",
    "3rk2r/pb3p2/2p1pbn1/1p6/2p2q2/P1N2B2/1PQ2PPP/3RK2R w Kk -",
    "3rk2r/pb3p2/2p1pbn1/1p6/2p2q2/P1N2B2/1PQ2PPP/3R1RK1 b k -",
    "3rk2r/pb3p2/2p1pbn1/1p6/2p5/P1N2B2/1PQ2PPq/3R1RK1 w k -"
]

### PATHS ###

# SOURCES
SQL_PGN_FILE = "pgnfiles/ficsgamesdb_2016_chess_nomovetimes_1482742.pgn" # 12309953 games 2016
SQL_DB_PATH = "chess.sqlite"
NEO4J_PGN_FILE = "pgnfiles/output.pgn" # 34382 games 2017 Jan >2000 Elo
NEO4J_DB_PATH = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASS = "pass"
NEO4J_GAME_INSERTS_PER_SESSION = 1000

# OUTPUT
DATA_OUTPUT_PATH = "assets/data/"
