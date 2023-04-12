import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b,cost))

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

start, end = map(int, input().split())
distance = dijkstra(graph, start)
# print(distance)
print(distance[end])
