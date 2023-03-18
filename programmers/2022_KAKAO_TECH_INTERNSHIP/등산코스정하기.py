import heapq
from collections import defaultdict

INF = int(1e9)

def get_min_intensity(n, graph, gates, summits):
        q = []
        distance = [INF] * (n + 1)
        for gate in gates:
            heapq.heappush(q, (0, gate))
            distance[gate] = 0

        while q:
            dist, node = heapq.heappop(q)

            if node in summits or distance[node] < dist:
                continue

            for weight, next_node in graph[node]:
                intensity = max(dist, weight)
                if intensity < distance[next_node]:
                    heapq.heappush(q, (intensity, next_node))
                    distance[next_node] = intensity
        summits = list(summits)
        summits = sorted(summits)
        answer = [0, INF]
        for summit in summits:
            intensity = distance[summit]
            if intensity < answer[1]:
                answer = [summit, intensity]
        return answer


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    summits = set(summits)
    for path in paths:
        i, j, weight = path
        graph[i].append((weight, j))
        graph[j].append((weight, i))
    
    return get_min_intensity(n, graph, gates, summits)

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5]))