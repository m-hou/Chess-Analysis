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

def main():
    """doc"""
    query_play_rate()

if __name__ == "__main__":
    main()
