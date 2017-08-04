"""doc"""

NUMBER_OF_COMMENTS = 2
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -"
STARTING_EVAL = 0.0

def transform(sequence, index):
    """doc"""
    def transform_moves(moves):
        """doc"""
        return moves

    def transform_fens(fens):
        """doc"""
        return [STARTING_FEN] + [" ".join(fen[2:-2].split(" ")[:-2]) for fen in fens]

    def transform_evals(evals):
        """doc"""
        return [STARTING_EVAL] + [eval[2:-2] for eval in evals]

    transformations = [transform_moves, transform_evals, transform_fens]
    return transformations[index](sequence)

def parse_move_comments(game):
    """doc"""
    partitions = NUMBER_OF_COMMENTS + 1
    return [transform(game.moves[i:-1:partitions], i) for i in range(partitions)]