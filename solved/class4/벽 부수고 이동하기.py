from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n,m = map(int, input().split())
graph = []
for i in range(n):
    temp = list(map(int, list(input())))
    graph.append(temp)
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs(n, m, graph, start):
    y, x = start
    queue = deque([(y, x, 0)])
    visited[y][x][0] = 1

    while queue:
        y, x, c = queue.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x][c]
        else:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                if graph[ny][nx] == 1 and c == 0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    queue.append((ny, nx, 1))
                elif graph[ny][nx] == 0 and visited[ny][nx][c] == 0:
                    visited[ny][nx][c] = visited[y][x][c] + 1
                    queue.append((ny, nx, c))
                    
    return -1

print(bfs(n, m, graph, (0,0)))