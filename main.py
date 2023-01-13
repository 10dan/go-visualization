import pickle
import helpers
import copy
from anytree import Node

# TODO: FIND TREE LIBRARY that takes [[arrays]] not just strings.
a = Node("test")
b = Node("pig", parent=a)
print(b)
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

def create_next_boards(board, parent_node):
    # Given current board, what states could be next?
    for x, row in enumerate(board):
        for y, stone in enumerate(row):
            # 0 empty, 1 black, 2 white
            if stone == 0:
                new_board = copy.deepcopy(parent_node)
                new_board[x][y] = whos_turn
                next_boards.append(new_board)
    print(next_boards)

whos_turn = 1
board = create_blank_board()
root = Node(board)
print(root)
create_next_boards(board)