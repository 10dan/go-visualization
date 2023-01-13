import pickle
import helpers
import copy

"""
Every GO board state will be represented in 3 states:
- A 3x3 integer array
    [ [0, 0, 1],
      [0, 2, 0],
      [1, 2, 0] ]
- A 18 bit binary string
    |        x - coord        |        y - coord         |
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
- A coordinate on a 2D plane
    Take the binary from above, and then scale between -100:100
    (-40, 50)
"""

def create_blank_board():
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

board = create_blank_board()

def create_next_boards(board):
    next_boards = []

    # Given current board, what states could be next?
    for x, row in enumerate(board):
        for y, stone in enumerate(row):
            # 0 empty, 1 black, 2 white
            if stone == 0:
                new_board = copy.deepcopy(board)
                new_board[x][y] = 1
                next_boards.append(new_board)
    print(next_boards)

create_next_boards(board)