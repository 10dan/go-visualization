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