import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().rstrip().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for temp_node, weight in graph[node]:
            cost = dist + weight
            if cost < distance[temp_node]:
                heapq.heappush(queue, (cost, temp_node))
                distance[temp_node] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])