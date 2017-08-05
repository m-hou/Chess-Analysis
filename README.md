# Chess Analysis

[Project Demo](https://m-hou.github.io/Chess-Analysis/)

Chess analysis is a project that allows you to aggregate data from chess games and render interesting visualizations with D3.js charts. This repository contains resources and scripts that allow you clean up portable game notation (PGN) files and store the data into Neo4j and SQLite databases.

Neo4j is used to store information about the moves in a game. A graph database fits well for this task, since game state is essentially a graph. SQLite is used to store game metadata, such as the player Elos, game result, time control, etc. This is quite standard, so a relational database works will for this task.

### Overview

`pgn-extract.exe` pre-processes pgn files to, for example, remove games without any moves. `setupdb.py` files will set up the schema for the databases. From here pgn files are fed to the `parser.py` files that will parse the pgn and insert all the data. `aggregate.py` files will query the databases and output the results to json files in the assets folder

### Usage

Step 1: Get PGN files
Find a pgn file online from a game database. I would recommend [FICS Games Database](http://ficsgames.org/download.html) as the data from this source is very clean.

Step 2: Clean up PGN files
Download `pgn-extract.exe` from the repository resources and run it with cmd or terminal to clean up the PGN files.

Here are the commands I use:

```
pgn-extract.exe -o clean.pgn -pl2 --nocomments -w1000000 <file_name.pgn>
pgn-extract.exe -o output.pgn -w1000000 --evaluation --fencomments clean.pgn
```

This first command will filter for games that have atleast 2 moves played, remove all extra comments, and output the result into `clean.pgn` with maximum one million characters on a line (this is used to ensure all moves in a game are output onto a single line). The second command will take `clean.pgn`, append the evaluation and fen after each move, and output the result to `output.pgn` with maximum one million characters on a line.

Step 3: Setup databases
For SQL, Create a `.sqlite` file and place it into the root folder. For Neo4j, create a database with Neo4j and have it running on the default port. Run the `setupdb.py` files to create the necessary tables and indicies for the databases.

Step 4: Set configurations
Use the `config.py` file to set up the configurations. Make sure the paths are all correct.

Step 5: Parse the data into the databases
Run the `parser.py` files to parse the data. This can take a while depending on how much data you have. The Neo4j script inserts at roughly 2 games/s and the SQLite script inserts at roughly 200 games/s.

Step 6: Generate the json files
Run the `aggregate.py` files to query the databases and output the json files used by d3. `config.py` comes with some settings for the aggregations.

Step 7: View charts
You can serve your webpage locally with the command: `python -m http.server`. After that, just visit `localhost:8000`

### Next Steps

In the future, it would be great to have a node.js backend set up so that the databases can be queried live. Additionaly, adding more aggregations can lead to discovering other interesting correlations.

### Contributors

My friend [Austin](https://github.com/ahendy) for playing chess with me at work and encouraging me to try out Python and start this project.

[Renatopp's PGNParser](https://github.com/renatopp/pgnparser), which I am using to help parse PGN files. The parser is written in Python 2.7, so I updated it (in my repo as `pgn.py`) to work for 3.6.

[Novus' nvd3](https://github.com/nvd3-community/nvd3), which I used to create the charts.
