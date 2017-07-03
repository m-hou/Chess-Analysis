"""doc"""

import sqlite3

DB_PATH = "chess.sqlite"

def eco_mapping(char, number):
    """doc"""
    opening_name = ""
    opening_sequence = ""
    if char == "A":
        if number == 0:
            opening_name = "Polish (Sokolsky) opening"
            opening_sequence = "b4"
        elif number == 1:
            opening_name = "Nimzovich-Larsen attack"
            opening_sequence = "b3"
        elif 2 <= number <= 3:
            opening_name = "Bird's opening"
            opening_sequence = "f4"
        elif 4 <= number <= 9:
            opening_name = "Reti opening"
            opening_sequence = "Nf3"
        elif 10 <= number <= 39:
            opening_name = "English opening"
            opening_sequence = "c4"
        elif 40 <= number <= 41:
            opening_name = "Queen's pawn"
            opening_sequence = "d4"
        elif number == 42:
            opening_name = "Modern defence, Averbakh system"
            opening_sequence = "d4, d6, c4, g6, Nc3, Bg7, e4"
        elif 43 <= number <= 44:
            opening_name = "Old Benoni defence"
            opening_sequence = "d4, c5"
        elif 45 <= number <= 46:
            opening_name = "Queen's pawn game"
            opening_sequence = "d4, Nf6"
        elif number == 47:
            opening_name = "Queen's Indian defence"
            opening_sequence = "d4, Nf6, Nf3, b6"
        elif 48 <= number <= 49:
            opening_name = "King's Indian, East Indian defence"
            opening_sequence = "d4, Nf6, Nf3, g6"
        elif number == 50:
            opening_name = "Queen's pawn game"
            opening_sequence = "d4, Nf6, c4"
        elif 51 <= number <= 52:
            opening_name = "Budapest defence"
            opening_sequence = "d4, Nf6, c4, e5"
        elif 53 <= number <= 55:
            opening_name = "Old Indian defence"
            opening_sequence = "d4, Nf6, c4, d6"
        elif number == 56:
            opening_name = "Benoni defence"
            opening_sequence = "d4, Nf6, c4, c5"
        elif 57 <= number <= 59:
            opening_name = "Benko gambit"
            opening_sequence = "d4, Nf6, c4, c5, d5, b5"
        elif 60 <= number <= 79:
            opening_name = "Benoni defence"
            opening_sequence = "d4, Nf6, c4, c5, d5, e6"
        elif 80 <= number <= 99:
            opening_name = "Dutch"
            opening_sequence = "d4, f5"
    elif char == "B":
        if number == 0:
            opening_name = "King's pawn opening"
            opening_sequence = "e4"
        elif number == 1:
            opening_name = "Scandinavian (centre counter) defence"
            opening_sequence = "e4, d5"
        elif 2 <= number <= 5:
            opening_name = "Alekhine's defence"
            opening_sequence = "e4, Nf6"
        elif number == 6:
            opening_name = "Robatsch (modern) defence"
            opening_sequence = "e4, g6"
        elif 7 <= number <= 9:
            opening_name = "Pirc defence"
            opening_sequence = "e4, d6, d4, Nf6, Nc3"
        elif 10 <= number <= 19:
            opening_name = "Caro-Kann defence"
            opening_sequence = "e4, c6"
        elif 20 <= number <= 99:
            opening_name = "Sicilian defence"
            opening_sequence = "e4, c5"
    elif char == "C":
        if 0 <= number <= 19:
            opening_name = "French defence"
            opening_sequence = "e4, e6"
        elif 0 <= number <= 20:
            opening_name = "King's pawn game"
            opening_sequence = "e4, e5"
        elif 21 <= number <= 22:
            opening_name = "Center game"
            opening_sequence = "e4, e5, d4, exd4"
        elif 23 <= number <= 24:
            opening_name = "Bishop's opening"
            opening_sequence = "e4, e5, Bc4"
        elif 25 <= number <= 29:
            opening_name = "Vienna game"
            opening_sequence = "e4, e5, Nc3"
        elif 30 <= number <= 39:
            opening_name = "King's gambit"
            opening_sequence = "e4, e5, Nf3"
        elif number == 40:
            opening_name = "King's knight opening"
            opening_sequence = "e4, e5, f4"
        elif number == 41:
            opening_name = "Philidor's defence"
            opening_sequence = "e4, e5, Nf3, d6"
        elif 42 <= number <= 43:
            opening_name = "Petrov's defence"
            opening_sequence = "e4, e5, Nf3, Nf6"
        elif number == 44:
            opening_name = "King's pawn game"
            opening_sequence = "e4, e5, Nf3, Nc6"
        elif number == 45:
            opening_name = "Scotch game"
            opening_sequence = "e4, e5, Nf3, Nc6, d4, exd4, Nxd4"
        elif number == 46:
            opening_name = "Three knights game"
            opening_sequence = "e4, e5, Nf3, Nc6, Nc3"
        elif 47 <= number <= 49:
            opening_name = "Four knight's game"
            opening_sequence = "e4, e5, Nf3, Nc6, Nc3, Nf6, d4"
        elif number == 50:
            opening_name = "King's pawn game"
            opening_sequence = "e4, e5, Nf3, Nc6, Bc4"
        elif 51 <= number <= 52:
            opening_name = "Evans gambit"
            opening_sequence = "e4, e5, Nf3, Nc6, Bc4, Bc5, b4"
        elif 53 <= number <= 54:
            opening_name = "Giuoco Piano"
            opening_sequence = "e4, e5, Nf3, Nc6, Bc4, Bc5, c3"
        elif 55 <= number <= 59:
            opening_name = "Two knights defence"
            opening_sequence = "e4, e5, Nf3, Nc6, Bc4, Nf6"
        elif 60 <= number <= 99:
            opening_name = "Ruy Lopez (Spanish opening)"
            opening_sequence = "e4, e5, Nf3, Nc6, Bb5"
    elif char == "D":
        if number == 0:
            opening_name = "Queen's pawn game"
            opening_sequence = "d4, d5"
        elif number == 1:
            opening_name = "Richter-Veresov attack"
            opening_sequence = "d4, d5, Nc3, Nf6, Bg5"
        elif number == 2:
            opening_name = "Queen's pawn game"
            opening_sequence = "d4, d5, Nf3"
        elif number == 3:
            opening_name = "Torre attack (Tartakower variation)"
            opening_sequence = "d4, d5, Nf3, Nf6, Bg5"
        elif 4 <= number <= 5:
            opening_name = "Queen's pawn game"
            opening_sequence = "d4, d5, Nf3, Nf6, e3"
        elif number == 6:
            opening_name = "Queen's Gambit"
            opening_sequence = "d4, d5, c4"
        elif 7 <= number <= 9:
            opening_name = "Queen's Gambit Declined, Chigorin defence"
            opening_sequence = "d4, d5, c4, Nc6"
        elif 10 <= number <= 15:
            opening_name = "Queen's Gambit Declined Slav defence"
            opening_sequence = "d4, d5, c4, c6"
        elif number == 16:
            opening_name = "Queen's Gambit Declined Slav accepted, Alapin variation"
            opening_sequence = "d4, d5, c4, c6, Nf3, Nf6, Nc3, dxc4, a4"
        elif 17 <= number <= 19:
            opening_name = "Queen's Gambit Declined Slav, Czech defence"
            opening_sequence = "d4, d5, c4, c6, Nf3, Nf6, Nc3, dxc4, a4, Bf5"
        elif 20 <= number <= 29:
            opening_name = "Queen's gambit accepted"
            opening_sequence = "d4, d5, c4, dxc4"
        elif 30 <= number <= 42:
            opening_name = "Queen's gambit declined"
            opening_sequence = "d4, d5, c4, e6"
        elif 43 <= number <= 49:
            opening_name = "Queen's Gambit Declined semi-Slav"
            opening_sequence = "d4, d5, c4, e6, Nc3, Nf6, Nf3, c6"
        elif 50 <= number <= 69:
            opening_name = "Queen's Gambit Declined, 4.Bg5"
            opening_sequence = "d4, d5, c4, e6, Nc3, Nf6, Bg5"
        elif 70 <= number <= 79:
            opening_name = "Neo-Gruenfeld defence"
            opening_sequence = "d4, Nf6, c4, g6, f3, d5"
        elif 80 <= number <= 99:
            opening_name = "Gruenfeld defence"
            opening_sequence = "d4, Nf6, c4, g6, Nc3, d5"
    elif char == "E":
        if number == 0:
            opening_name = "Queen's pawn game"
            opening_sequence = "d4, Nf6, c4, e6"
        elif 1 <= number <= 9:
            opening_name = "Catalan, closed"
            opening_sequence = "d4, Nf6, c4, e6, g3, d5, Bg2"
        elif number == 10:
            opening_name = "Queen's pawn game"
            opening_sequence = "d4, Nf6, c4, e6, Nf3"
        elif number == 11:
            opening_name = "Bogo-Indian defence"
            opening_sequence = "d4, Nf6, c4, e6, Nf3, Bb4+"
        elif 12 <= number <= 19:
            opening_name = "Queen's Indian defence"
            opening_sequence = "d4, Nf6, c4, e6, Nf3, b6"
        elif 20 <= number <= 59:
            opening_name = "Nimzo-Indian defence"
            opening_sequence = "d4, Nf6, c4, e6, Nc3, Bb4"
        elif 60 <= number <= 99:
            opening_name = "King's Indian defence"
            opening_sequence = "d4, Nf6, c4, g6"
    return (u'%s%02d' % (char, number), opening_name, opening_sequence,)

def main():
    """doc"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("pragma foreign_keys=ON")
    try:
        c.execute(
            """
            CREATE TABLE Eco (
                code STRING not null,
                openingName STRING not null,
                openingSequence STRING not null,
                PRIMARY KEY (code));
            """
        )
    except sqlite3.OperationalError:
        pass
    try:
        c.execute(
            """
            CREATE TABLE TimeControl (
                time INTEGER not null,
                increment INTEGER not null,
                formatName STRING,
                PRIMARY KEY (time, increment));
            """
        )
    except sqlite3.OperationalError:
        pass
    try:
        c.execute(
            """
            CREATE TABLE Games (
                result STRING not null,
                year INTEGER not null,
                month INTEGER not null,
                whiteElo INTEGER not null,
                blackElo INTEGER not null,
                code STRING not null REFERENCES Eco(code),
                time INTEGER not null,
                increment INTEGER not null,
                gameid STRING not null,
                PRIMARY KEY (gameid),
                FOREIGN KEY (time, increment) REFERENCES TimeControl(time, increment))
            """
        )
    except sqlite3.OperationalError:
        pass
    conn.commit()
    for char in "ABCDE":
        for number in range(100):
            c.execute("""INSERT INTO Eco
                        VALUES (?,?,?)""", eco_mapping(char, number))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
