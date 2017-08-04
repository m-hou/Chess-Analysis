# Chess-Analysis

[Demo](https://m-hou.github.io/Chess-Analysis/)

Aggregate data from chess games and render interesting visualizations with D3.js charts

This repository contains resources and scripts that allow you clean up portable game notation (PGN) files and store the data into Neo4j and SQLite databases.

Neo4j is used to store information about the moves in a game. A graph database fits well for this task, since game state is essentially a graph.

SQLite is used to store game metadata, such as the player Elos, game result, time control, etc. A relational database works will for this task, since...

### Overview

pgn-extract.exe pre-processes pgn files to, for example, remove games without any moves. setupdb.py files will set up the schema for the databases. From here pgn files are fed to the parser.py files that will parse the pgn and insert all the data. aggregate.py files will query the databases and output the results to json files in the assets folder

### Usage

Step 1: Get PGN files
Find a pgn file online from a game database. I would recommend [FICS Games Database](http://ficsgames.org/download.html), the data for this source is very clean.

Step 2: Clean up PGN files
Download pgn-extract.exe from the repository resources and run it with cmd or terminal to clean up the PGN files.

Here are the commands I use:

pgn-extract.exe -o clean.pgn -pl2 --nocomments -w1000000 <file_name.pgn>
pgn-extract.exe -o output.pgn -w1000000 --evaluation --fencomments clean.pgn

This first command will filter for games that have atleast 2 moves played, remove all extra comments, and output the result into clean.pgn with maximum one million characters on a line (this is used to output all the moves in a game on a single line, without any breaks). The second command will take clean.pgn, append the evaluation and fen after each move, and output the result to output.pgn with maximum one million characters on a line.

Step 3: Setup databases
For SQL, Create a file called games.sql and place it into the root folder. For neo4j, create a database with neo4j and have it running. Run the setupdb.py files to create the necessary tables and indicies for the databases.

Step 4: Parse the data into the databases
Replace the file names in the parser.py files to match the PGN files that you have and run the parser.py files to parse the data. This can take a while depending on how much data you have. The script for neo4j inserts at roughly 2 games/s and for SQLite, roughly 200 games/s.

Step 5: Generate the json files
Run the aggregate.py files to query the databases and output the json files used by d3.

Step 6: View charts
You can serve your webpage locally with the command: python -m http.server. After that, just visit localhost:8000

### Next Steps

Future plans involve setting up a node.js backend so that the databases can be queried live. Having configuration files would also make forking the repository and aggregating your own games easier.

### Contributors

My friend [Austin](https://github.com/ahendy) for playing chess with me and inspiring me to start this project along with encouraging me to try out Python.

[Renatopp's PGNParser](https://github.com/renatopp/pgnparser), which I am using to help parse PGN files. The parser is written in Python 2.7, so I updated it (in my repo as pgn.py) to work for 3.6.
