import pickle
import helpers
import go
import copy

"""
Every GO board state will be represented in 3 states:
- A 3x3 integer array
    [ [0, 0, 1],      | 0 1 2
      [0, 2, 0],      | 3 4 5
      [1, 2, 0] ]     | 6 7 8
- A 18 bit binary string
    |        x - coord        |        y - coord         |
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
- A coordinate on a 2D plane
    Take the binary from above, and then scale between -100:100
    (-40, 50)
"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

root = TreeNode([[1, 2], [3, 4]])
child1 = TreeNode([[5, 6], [7, 8]])
child2 = TreeNode([[9, 10], [11, 12]])
root.children.append(child1)
root.children.append(child2)

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

print(root)
create_next_boards(board)