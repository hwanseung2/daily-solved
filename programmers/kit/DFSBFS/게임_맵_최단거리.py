# INF = int(1e9)

# def dfs(maps, y, x, cnt):
#     global answer
#     n = len(maps)
#     m = len(maps[0])
#     if y == n-1 and x == m-1:
#         answer = min(answer, cnt)
#         return
    
#     if y < 0 or x < 0 or y >= n or x >= m:
#         return
#     if maps[y][x] == 1:
#         maps[y][x] = 2
#         dfs(maps, y-1, x, cnt + 1)
#         dfs(maps, y, x+1, cnt + 1)
#         dfs(maps, y+1, x, cnt + 1)
#         dfs(maps, y, x-1, cnt + 1)

# def solution(maps):
#     global answer
#     answer = INF

#     dfs(maps, 0, 0, 1)
#     if answer == INF:
#         return -1
#     else:
#         return answer

from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
INF = int(1e9)

def solution(maps):
    answer = INF
    n = len(maps)
    m = len(maps[0])
    queue = deque([(0,0, 1)])
    maps[0][0] = 2
    
    while queue:
        y, x, cnt = queue.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if maps[ny][nx] == 1:
                maps[ny][nx] = 2
                queue.append((ny, nx, cnt + 1))
    
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))