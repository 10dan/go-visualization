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

def create_blank_board():
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

def create_next_boards(board, parent_node, player):
    """
    board: 2d array, current board state.
    parent_node: the TreeNode of the parent.
    players: 1 or 2 for black or white.
    """

    # Given current board, what states could be next?
    for x, row in enumerate(board):
        for y, _ in enumerate(row):
            if go.is_legal_move(board, x,y,player):
                new_board = copy.deepcopy(board)
                new_board[x][y] = player
                parent_node.children.append(new_board)
                
def turn_calc():
    if player_one_turn:
        player_one_turn = not player_one_turn
        return 1
    else:
        player_one_turn = not player_one_turn
        return 2

player_one_turn = True



board = create_blank_board()
root = TreeNode(board)
create_next_boards(board, root, turn_calc())
print(root.children)

for child in root.children:
    create_next_boards(child, TreeNode(child), turn_calc())