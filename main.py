import pickle
import helpers
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
    
def is_legal_move(board, x, y, player):
    # Check if the move is within the board boundaries
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        return False

    # Check if the selected cell is not occupied
    if board[x][y] != 0:
        return False

    # Check if the move captures any opponent's stones
    opponent = 3 - player
    captured = check_captures(board, x, y, opponent)

    # Check if the move does not leave the player's own group in a captured state
    return not check_captures(board, x, y, player)

def check_captures(board, x, y, player):
    captures = False

    # Check in all four directions
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if check_captures_direction(board, x, y, dx, dy, player):
            captures = True

    return captures

def check_captures_direction(board, x, y, dx, dy, player):
    captures = False

    # Check if the next cell in the direction is occupied by the opponent
    x2, y2 = x + dx, y + dy
    if x2 < 0 or x2 >= len(board) or y2 < 0 or y2 >= len(board[0]) or board[x2][y2] != player:
        return captures

    # Check if the group has any liberties
    liberties = check_group_liberties(board, x2, y2, player)
    if liberties == 0:
        captures = True
    return captures

def check_group_liberties(board, x, y, player):
    liberties = 0
    visited = set()
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)
        visited.add((x, y))
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x2, y2 = x + dx, y + dy
            if x2 < 0 or x2 >= len(board) or y2 < 0 or y2 >= len(board[0]):
                continue
            if board[x2][y2] == 0:
                liberties += 1
            elif board[x2][y2] == player and (x2, y2) not in visited:
                queue.append((x2, y2))
    return liberties

whos_turn = 1
board = create_blank_board()

print(root)
create_next_boards(board)