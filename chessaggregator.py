"""doc"""

import sqlite3
import tools

DB_PATH = "chess.sqlite"
MIN_ELO = 0
MAX_ELO = 3000
INCREMENT = 25

def query_db(query, *args):
    """doc"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(query, *args)
    print(c.fetchall())
    conn.commit()
    conn.close()

@tools.timedcall
def query_play_rate():
    """doc"""
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
            Games.blackElo >= EloRanges.elo and Games.blackElo < EloRanges.elo + ?
            GROUP BY EloRanges.elo, Eco.openingName
        ) GROUP BY opening
        ORDER BY SUM(frequency) DESC LIMIT 20
        """,
        (MIN_ELO, INCREMENT, MAX_ELO, INCREMENT))

def main():
    """doc"""
    query_play_rate()

if __name__ == "__main__":
    main()
