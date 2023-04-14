# import sys
# from collections import defaultdict

# sys.setrecursionlimit(int(1e7))
# input = sys.stdin.readline

# def dfs(node, root):
#     global visited, graph, teams
#     if node in teams:
#         return False

#     if graph[node] == root:
#         visited[node] = True
#         teams.add(node)
#         return True
    
#     if visited[node] == True:
#         return False
#     if node == graph[node]:
#         visited[node] = True
#         teams.add(node)
#         return False

#     flag = dfs(graph[node], root)
#     if flag == True:
#         visited[node] = True
#         teams.add(node)
#         return True
#     else:
#         visited[node] = False
#         return False


# T = int(input().rstrip())
# for _ in range(T):
#     teams = set()
#     n = int(input().rstrip())
#     ary = list(map(int, input().split()))
#     graph = defaultdict(int)
#     for i in range(1, n+1):
#         node = ary[i-1]
#         graph[i] = node

#     visited = [False] * (n+1)

#     for i in range(1, n+1):
#         flag = dfs(i, i)
#     answer = 0
#     for idx in range(1, n+1):
#         if visited[idx] == False:
#             answer += 1
#     print(answer)
        

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())
 
def dfs(x):
    global cnt
    visited[x] = True
    i = graph[x]
    if not visited[i]:
        dfs(i)
    else:
        if i not in team:
            nxt = i
            while nxt != x:
                cnt += 1
                nxt = graph[nxt]
            cnt += 1
 
    team.add(x)
 
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    team = set()
 
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
 
    print(n - cnt)