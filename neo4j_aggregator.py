"""doc"""

import json
from collections import defaultdict
import tools
from neo4j.v1 import GraphDatabase, basic_auth

DB_PATH = "bolt://localhost:7687"
OUT_FILE = "assets/data_chart5.json"

HARDCODED_FENS = [
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

def generate_next_moves():
    """doc"""
    for fen in HARDCODED_FENS:
        get_next_moves(fen)

def query_db(query, parser, args=None, out_file=OUT_FILE):
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "pass"))
    session = driver.session()
    result = session.run(query, args)
    data = parser(result)
    session.close()
    with open("assets/" + out_file.replace("/", "_"), 'w') as outfile:
        json.dump(data, outfile)


@tools.timedcall
def get_next_moves(fen):
    """doc"""
    def next_moves_parser(result):
        """doc"""
        def classify_move(move):
            """doc"""
            if "x" in move:
                return "Capture"
            elif move == "O-O" or move == "O-O-O":
                return "Castling"
            elif len(move) == 2:
                return "Pawn Push"
            else:
                return "Move"

        values = list(result)
        games_played = sum(record["freq"] for record in values)
        point_attributes = [dict(key=classify_move(record["move"]),
                                 value=dict(x=record["freq"] / games_played,
                                            y=record["winRate"],
                                            size=1,
                                            shape="square",
                                            move=record["move"]))
                            for record in values]
        d = defaultdict(list)
        for point_attribute in point_attributes:
            d[point_attribute["key"]].append(point_attribute["value"])
        return [dict(key=k, values=v) for k, v in d.items()]

    query_db(
        """
        MATCH (:Position {fen: {fen}})-[m:Move]->(next:Position)
        MATCH (next)-[:Move|FinalPosition*..1000]-[:FinalPosition]-(g:Game) WITH DISTINCT g, m
        RETURN m.move AS move, AVG(
            CASE g.result
                WHEN '1-0' THEN 1
                WHEN '1/2-1/2' THEN 0.5
                WHEN '0-1' THEN 0
            END
        ) AS winRate, count(g) AS freq""",
        next_moves_parser,
        {"fen": fen},
        fen + ".json"
    )


@tools.timedcall
def get_avg_eval_by_ply():
    """doc"""
    def avg_eval_by_ply_parser(result):
        """doc"""
        return [dict(values=[dict(x=record["ply"], y=record["averageEval"])
                             for record in list(result)])]

    query_db(
        """
        MATCH (p:Ply)-[:HasPosition]->(pos:Position)
        RETURN p.moveNumber AS ply, AVG(TOFLOAT(pos.eval)) AS averageEval
        ORDER BY p.moveNumber""",
        avg_eval_by_ply_parser
    )


@tools.timedcall
def get_eval_range_by_time_control():
    """doc"""
    def eval_range_by_time_control_parser(result):
        """doc"""
        def parse_record(record):
            """doc"""
            return dict(Q1=record["percentile25"],
                        Q2=record["percentile50"],
                        Q3=record["percentile75"],
                        whisker_low=record["min"],
                        whisker_high=record["max"])

        return [dict(label=record["timeControl"], values=parse_record(record))
                for record in list(result)]

    query_db(
        """
        MATCH (g:Game)-[:HasPosition|:FinalPosition]->(p:Position)
            WITH g, max(TOFLOAT(p.eval)) - min(TOFLOAT(p.eval)) AS EvalRange
        RETURN
        g.timecontrol AS timeControl,
        max(EvalRange) as max,
        percentileCont(EvalRange, .75) AS percentile75,
        percentileCont(EvalRange, .50) AS percentile50,
        percentileCont(EvalRange, .25) AS percentile25,
        min(EvalRange) AS min""",
        eval_range_by_time_control_parser
    )


def main():
    """doc"""
    generate_next_moves()


if __name__ == "__main__":
    main()
