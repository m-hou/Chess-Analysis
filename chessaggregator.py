"""doc"""

import json
import sqlite3
import tools

DB_PATH = "chess.sqlite"
OUT_FILE = "assets/data_chart2.json"
MIN_ELO = 0
MAX_ELO = 3000
INCREMENT = 25

def query_db(query, parser, *args):
    """doc"""

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(query, *args)
    data = parser(c.fetchall())
    conn.close()
    with open(OUT_FILE, 'w') as outfile:
        json.dump(data, outfile)

@tools.timedcall
def query_play_rate():
    """doc"""
    def play_rate_parser(raw_data):
        """doc"""
        def parse_freq_str(freq_str):
            """doc"""
            elos = range(MIN_ELO, MAX_ELO + INCREMENT, INCREMENT)
            freqs = map(int, freq_str.split(","))
            return list(zip(elos, freqs))

        return [dict(key=opening, values=parse_freq_str(freq_str))
                for opening, freq_str in raw_data]

    query_db(
        """
        SELECT opening, GROUP_CONCAT(frequency) frequency
        FROM (
            WITH RECURSIVE
                EloRanges(elo) AS (VALUES(?) UNION ALL SELECT elo + ? FROM EloRanges WHERE elo < ?)
            SELECT EloRanges.elo elo, Eco.openingName opening,
                SUM(CASE WHEN Games.gameid IS NULL THEN 0 ELSE 1 END) AS frequency
            FROM Eco, EloRanges
            LEFT JOIN Games ON Games.code = Eco.code AND
            (Games.blackElo + Games.whiteElo) / 2 >= EloRanges.elo AND
            (Games.blackElo + Games.whiteElo) / 2 < EloRanges.elo + ?
            GROUP BY EloRanges.elo, Eco.openingName
        ) GROUP BY opening
        ORDER BY SUM(frequency) DESC LIMIT 20
        """,
        play_rate_parser,
        (MIN_ELO, INCREMENT, MAX_ELO, INCREMENT))

@tools.timedcall
def query_win_rate():
    """doc"""
    def win_rate_parser(raw_data):
        """doc"""
        opening, wins, draws, losses = list(zip(*raw_data))
        return [dict(key=result,
                     values=[dict(x=opening, y=count)
                             for opening, count in stat_iter])
                for result, stat_iter in zip(["White wins", "Draws", "Black wins"], [zip(opening, wins), zip(opening, draws), zip(opening, losses)])]
    query_db(
        """
        SELECT Eco.openingName,
        SUM(CASE WHEN Result = "1-0" THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN RESULT = "1/2-1/2" THEN 1 ELSE 0 END) as ties,
        SUM(CASE WHEN RESULT = "0-1" THEN 1 ELSE 0 END) as losses
        FROM Games
        INNER JOIN Eco ON Games.code = Eco.code
        GROUP BY Eco.openingName
        ORDER BY ((wins + ties / 2) * 1.0 / (wins + ties + losses)) DESC LIMIT 20
        """,
        win_rate_parser)

def main():
    """doc"""
    query_win_rate()

if __name__ == "__main__":
    main()
