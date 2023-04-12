from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_range = -1
for i in range(n):
    max_range = max(max_range, max(graph[i]))

def bfs(n, graph, start, visited, thre):
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if graph[ny][nx] <= thre:
                continue
            if visited[ny][nx] == True:
                continue
            queue.append((ny, nx))
            visited[ny][nx] = True
    return visited


answer = []
for thre in range(max_range + 1):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= thre:
                continue
            elif visited[i][j] == True:
                continue
            else:
                count += 1
                visited = bfs(n, graph, (i, j), visited, thre)
    answer.append(count)

print(max(answer))