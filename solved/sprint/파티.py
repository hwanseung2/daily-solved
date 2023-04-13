# import sys
# import heapq

# INF = int(1e9)

# input = sys.stdin.readline
# n, m, x = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     graph[a].append((b, cost))

# def dijkstra(graph, start):
#     distance = [INF] * (n+1)
#     distance[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))

#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for next, next_dist in graph[now]:
#             cost = dist + next_dist
#             if cost < distance[next]:
#                 distance[next] = cost
#                 heapq.heappush(q, (cost, next))
#     return distance

# result = [0] * (n+1)
# for start in range(1, n+1):
#     if start == x:
#         continue
#     distance = dijkstra(graph, start)
#     result[start] += distance[x]

# distance = dijkstra(graph, x)
# for i in range(1, n+1):
#     if i == x:
#         continue
#     result[i] += distance[i]

# print(max(result[1:]))

import sys
import heapq

INF = int(1e9)

input = sys.stdin.readline
n, m, x = map(int, input().split())
graph_origin = [[] for _ in range(n+1)]
graph_reverse = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph_origin[a].append((b, cost))
    graph_reverse[b].append((a, cost))

def dijkstra(graph, start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance

result = [0] * (n+1)
distance = dijkstra(graph_reverse, x)
for i in range(1, n+1):
    if i == x:
        continue
    result[i] += distance[i]

distance = dijkstra(graph_origin, x)
for i in range(1, n+1):
    if i == x:
        continue
    result[i] += distance[i]

print(max(result[1:]))