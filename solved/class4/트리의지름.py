# import sys
# from collections import defaultdict

# input = sys.stdin.readline
# V = int(input().rstrip())
# graph = defaultdict(list)
# starts = []

# for _ in range(V):
#     temp = list(map(int, input().rstrip().split()))
#     node, end = temp[0], temp[-1]
#     info = temp[1:-1]
#     for i in range(0, len(info), 2):
#         link, weight = info[i], info[i+1]
#         graph[node].append((link, weight))
#     if len(graph[node]) == 1:
#         starts.append(node)

# answer = -1
# visited = [False] * (V + 1)
# visited[0] = True
# leafs = []

# def dfs(graph, start, count):
#     # print(start)
#     global answer, leafs
#     flag = False
#     for node, weight in graph[start]:
#         flag = flag or not visited[node]
#     if flag == False:
#         answer = max(answer, count)
#         leafs.append(start)
#         return

#     for node, weight in graph[start]:
#         if visited[node] == False:
#             visited[node] = True
#             dfs(graph, node, count + weight)
#             visited[node] = False

# for start in starts:
#     if start in leafs:
#         continue

#     visited[start] = True
#     # print(f"[START]: {start}, [VISITED]: {visited}")
#     dfs(graph, start, 0)
#     visited[start] = False
#     # print('\n\n')

# print(answer)
import sys
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
# 2차원 리스트에 트리 저장(연결 그래프)
for _ in range(V):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2

visited = [-1]*(V+1)
visited[1] = 0

# 리턴 값 없음. visited에 모든 노드까지의 거리 저장
def DFS(node, dist):
    for v, d in tree[node]:
        cal_dist = dist + d
        if visited[v] == -1:
            visited[v] = cal_dist
            DFS(v, cal_dist)
    return
            
DFS(1, 0)
tmp = [0, 0]
# 최대 거리에 있는 노드 찾기
for i in range(1, len(visited)):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i

# 찾은 노드와, 찾은 노드에서 DFS 돌려 찾은 최대 거리 노드가 지름의 양 끝점
# 이 논리의 증명은 따로 알아보자
# 논리 : 임의의 노드에서 최대 거리에 있는 노드는 반드시 트리의 지름의 양 끝점 중 하나이다.
visited = [-1]*(V+1)
visited[tmp[0]] = 0
DFS(tmp[0], 0)

print(max(visited))