"""doc"""

import json
from collections import defaultdict
import config
import tools
from neo4j.v1 import GraphDatabase, basic_auth
import neo4j_tools
import pgn


def get_game():
    """doc"""
    games = pgn.GameIterator(config.NEO4J_PGN_FILE)
    for game in games:
        if game.ficsgamesdbgameno == config.GAMEID:
            return game


def extract_game_data():
    """doc"""
    def format_moves(moves):
        """doc"""
        return ' '.join((str(index // 2 + 1) + ". ") * (index % 2 == 0) + move
                        for index, move in enumerate(moves))


    moves, _, fens = neo4j_tools.parse_move_comments(get_game())
    with open(config.DATA_OUTPUT_PATH + "selected_game_moves.txt", 'w') as outfile:
        outfile.write(format_moves(moves))
    generate_next_moves(fens)


def generate_next_moves(fens):
    """doc"""
    for fen in fens:
        get_next_moves(fen)


def query_db(query, out_file_name, parser, args=None):
    """doc"""
    driver = GraphDatabase.driver(config.NEO4J_DB_PATH, auth=basic_auth(config.NEO4J_USER, config.NEO4J_PASS))
    with driver.session() as session:
        result = session.run(query, args)
        data = parser(result)
        with open(config.DATA_OUTPUT_PATH + out_file_name.replace("/", "_"), 'w') as outfile:
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
        print(str(len(point_attributes)) + " different moves found from this position")
        d = defaultdict(list)
        for point_attribute in point_attributes:
            d[point_attribute["key"]].append(point_attribute["value"])
        return [dict(key=k, values=v) for k, v in d.items()]

    query_db(
        """
        MATCH (:Position {fen: {fen}})-[m:Move]->(next:Position)
        MATCH (next)-[:Move*0..1000]->()<-[:FinalPosition]-(g:Game) WITH DISTINCT g, m
        RETURN m.move AS move, AVG(
            CASE g.result
                WHEN '1-0' THEN 1
                WHEN '1/2-1/2' THEN 0.5
                WHEN '0-1' THEN 0
            END
        ) AS winRate, count(g) AS freq""",
        fen + ".json",
        next_moves_parser,
        {"fen": fen},
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
        "chart4.json",
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
        "chart3.json",
        eval_range_by_time_control_parser
    )


def main():
    """doc"""
    if config.CHART_3:
        get_avg_eval_by_ply()
    if config.CHART_4:
        get_eval_range_by_time_control()
    if config.CHART_5:
        extract_game_data()


if __name__ == "__main__":
    main()
