# import sys
# sys.setrecursionlimit(int(1e6))
# ANSWER = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# INF = int(1e9)
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# def dfs(graph, y, x, cnt):
#     global answer
#     if y == 2 and x == 2:
#         flag = True
#         for i in range(3):
#             for j in range(3):
#                 if graph[i][j] != ANSWER[i][j]:
#                     flag = False
#         if flag:
#             answer = min(answer, cnt)
#         else:
#             return
    
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if ny < 0 or nx < 0 or ny >= 3 or nx >= 3:
#             continue
#         if ANSWER[y][x] == graph[ny][nx]:
#             graph[y][x], graph[ny][nx] = graph[ny][nx], graph[y][x]
#             dfs(graph, ny, nx, cnt + 1)
#             graph[y][x], graph[ny][nx] = graph[ny][nx], graph[y][x]

# if __name__ == '__main__':
#     answer = INF
#     graph = [list(map(int, input().split())) for _ in range(3)]
#     start = [0, 0]
#     for i in range(3):
#         for j in range(3):
#             if graph[i][j] == 0:
#                 start = [i, j]
#     dfs(graph, start[0], start[1], 0)
#     if answer == INF:
#         print(-1)
#     else:
#         print(answer)

# from collections import deque

# ANSWER = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# INF = int(1e9)
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# visited = [[False] * 3 for _ in range(3)]
# def bfs(graph, y, x):
#     global answer
#     q = deque([])
#     q.append((start[0], start[1], 0))
#     visited[start[0]][start[1]] = True

#     while q:
#         y, x, cnt = q.popleft()
#         if y == 2 and x == 2:
#             answer = cnt
#             return 
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny < 0 or nx < 0 or ny >= 3 or nx >= 3:
#                 continue
#             if ANSWER[y][x] != graph[ny][nx]:
#                 continue
#             if visited[ny][nx] == False:
#                 q.append((ny, nx, cnt + 1))
#                 visited[ny][nx] = True

# if __name__ == '__main__':
#     answer = INF
#     graph = [list(map(int, input().split())) for _ in range(3)]
#     start = [0, 0]
#     for i in range(3):
#         for j in range(3):
#             if graph[i][j] == 0:
#                 start = [i, j]
#     bfs(graph, start[0], start[1])
#     if answer == INF:
#         print(-1)
#     else:
#         print(answer)

# from collections import deque, defaultdict
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# puzzle = ""
# for i in range(3):
#     puzzle += ''.join(list(input().split()))

# def bfs(puzzle):
#     q = deque([])
#     q.append(puzzle)
#     visited = defaultdict(int)
#     visited[puzzle] = 0
    
#     while q:
#         puzzle = q.popleft()
#         cnt = visited[puzzle]
#         coord = puzzle.index('0')

#         if puzzle == '123456780':
#             return cnt
        
#         y = coord // 3
#         x = coord % 3
#         cnt += 1
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny < 0 or nx < 0 or ny >= 3 or nx >= 3:
#                 continue
#             new_coord = ny * 3 + nx
#             puzzle_list = []
#             puzzle_list[coord], puzzle_list[new_coord] = puzzle_list[new_coord], puzzle_list[coord]
#             new_puzzle = ''.join(puzzle_list)

#             if visited.get(new_puzzle) == None:
#                 visited[new_puzzle] = cnt
#                 q.append(new_puzzle)
#     return -1

# print(bfs(puzzle))

from collections import deque

# 퍼즐을 문자열 123456780로 정렬시킨다고 생각하자
puzzle = ""
for i in range(3):
    puzzle += "".join(list(input().split()))

# 현재 puzzle의 모습을 key로, 움직인 횟수를 value로 저장
visited = {puzzle:0}
q = deque([puzzle])

# 상하좌우로 0(빈칸)을 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    while q:
        puzzle = q.popleft()
        cnt = visited[puzzle]
        z = puzzle.index('0') # 0(빈칸)의 위치
        
        if puzzle == '123456780':
            return cnt
        
        x = z // 3 # 2차원 배열의 행
        y = z % 3 # 2차원 배열의 열
        
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2 and 0 <= ny <= 2: # 이동 가능한 위치일 경우
                # nx, ny를 다시 리스트의 인덱스로 바꾸자
                nz = nx * 3 + ny
                puzzle_list = list(puzzle) # 원소 스와핑을 위해 문자열을 리스트로 바꾸자
                puzzle_list[z], puzzle_list[nz] = puzzle_list[nz], puzzle_list[z]
                new_puzzle = "".join(puzzle_list) # 딕셔너리를 위해 다시 문자열로
                
                # 방문하지 않았다면
                if visited.get(new_puzzle, 0) == 0:
                    visited[new_puzzle] = cnt 
                    q.append(new_puzzle)
                    
    return -1
                    
print(bfs())
