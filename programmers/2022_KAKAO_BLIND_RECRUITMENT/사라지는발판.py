dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

INF = int(1e9)
def in_range(board, y, x):
    if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]):
        return False
    return True

def is_finished(board, y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(board, ny, nx) and board[ny][nx] == 1:
            return False
    return True

def solve(board, y1, x1, y2, x2):
    if is_finished(board, y1, x1):
        return [False, 0]

    if y1 == y2 and x1 == x2:
        return [True, 1]
    
    min_turn = INF
    max_turn = 0
    can_win = False

    for i in range(4):
        ny = y1 + dy[i]
        nx = x1 + dx[i]
        if in_range(board, ny, nx) == False or board[ny][nx] == 0:
            continue

        board[y1][x1] = 0
        result = solve(board, y2, x2, ny, nx)
        board[y2][x2] = 1

        if result[0] == False:
            can_win = True
            min_turn = min(min_turn, result[1])
        elif can_win == False:
            max_turn = max(max_turn, result[1])
        
    turn = min_turn if can_win == True else max_turn

    return [can_win, turn + 1]

def solution(board, aloc, bloc):
    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]

