"""doc"""

import json
import tools
from neo4j.v1 import GraphDatabase, basic_auth

DB_PATH = "bolt://localhost:7687"
OUT_FILE = "assets/data_chart3.json"

def query_db(query, parser, args=None):
    """doc"""
    driver = GraphDatabase.driver(DB_PATH, auth=basic_auth("neo4j", "pass"))
    session = driver.session()
    result = session.run(query, args)
    data = parser(result)
    session.close()
    with open(OUT_FILE, 'w') as outfile:
        json.dump(data, outfile)

@tools.timedcall
def get_next_moves():
    """doc"""
    def next_moves_parser(result):
        """doc"""
        counter = 0
        for record in result:
            counter += 1
            print("%s %s %s" % (record["move"], record["winRate"], record["freq"]))
        print(counter)

    query_db(
        """
        MATCH (:Position {fen: {fen}})-[m:Move]->(next:Position)
        MATCH (next)-[:Move*..1000]->()<-[:FinalPosition]-(g:Game) WITH DISTINCT g, m
        RETURN m.move AS move, AVG(
            CASE g.result
                WHEN '1-0' THEN 1
                WHEN '1/2-1/2' THEN 0.5
                WHEN '0-1' THEN 0
            END
        ) AS winRate, count(g) AS freq""",
        next_moves_parser,
        {"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq"}
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
    get_eval_range_by_time_control()

if __name__ == "__main__":
    main()
