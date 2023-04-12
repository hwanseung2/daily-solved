# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# def is_possible(y, x, ny, nx, graph):
#     global n, m 
#     if ny < 0 or nx < 0 or ny >= n or nx >= m :
#         return False
#     else:
#         if graph[ny][nx] >= graph[y][x]:
#             return False
#         else:
#             return True

# def dfs(y, x, graph):
#     global n, m, answer
#     if y == n-1 and x == m-1:
#         answer += 1
#         return 
    
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if is_possible(y, x, ny, nx, graph):
#             dfs(ny, nx, graph)

# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     graph = [list(map(int, input().split())) for _ in range(n)]
#     answer = 0
#     dfs(0, 0, graph)
#     print(answer)

import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(y, x):
    if y == n-1 and x == m-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]
    
    ways = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= m or graph[ny][nx] >= graph[y][x]:
            continue
        ways += dfs(ny, nx)
        # if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] < graph[y][x]:
        #     ways += dfs(ny, nx)
    
    dp[y][x] = ways

    return dp[y][x]


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


answer = dfs(0, 0)

for i in range(n):
    print(dp[i])
print()

print(answer)