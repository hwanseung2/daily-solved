import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))

dy = [-1, 0, 1]
dx = [1, 1, 1]

def dfs(y, x):
    global answer
    if x == m-1:
        answer += 1
        return True
    
    for i in range(1, 4):
        ny = y + dy[i-1]
        nx = x + dx[i-1]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        if graph[ny][nx] != 0:
            continue
        
        graph[ny][nx] = i
        flag = dfs(ny, nx)
        if flag:
            return True
        
    return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    answer = 0
    visited = [[0] * m for _ in range(n)]

    for _ in range(n):
        temp = input().rstrip()
        temp = temp.replace('.', '0')
        temp = temp.replace('x', '1')
        temp = list(map(int, list(temp)))
        graph.append(temp)
    
    for i in range(n):
        dfs(i, 0)
    
    print(answer)