# import sys
# input = sys.stdin.readline


# def main(n, k, items, bags):
#     items.sort(key = lambda x: (-x[1], -x[0]))
#     bags.sort()
#     visited = [False] * k

#     answer = 0
#     print(items)
#     print(bags)
#     print()
#     for i in range(n):
#         start, end = 0, k-1
#         m, v = items[i]
#         visit_ptr = None
#         while start <= end:
#             mid = (start + end) // 2
#             if m <= bags[mid] and visited[mid] == False:
#                 end = mid - 1
#                 visit_ptr = mid
#             else:
#                 start = mid + 1
#         print(visit_ptr, visited)
#         if visit_ptr != None:
#             visited[visit_ptr] = True
#             answer += v
#         else:
#             continue

#     print(answer)

# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     items = [list(map(int, input().split())) for _ in range(n)]
#     bags = [int(input().rstrip()) for _ in range(k)]

#     main(n, k, items, bags)
#     """
#     반례:
#     3 3
#     10 10
#     20 20
#     30 30
#     30
#     20
#     10
#     답: 60, 예측값: 50
#     """

import sys
import heapq
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input().rstrip()) for _ in range(k)]

gems.sort()
bags.sort()
q = deque(gems)

result = 0
tmp = []

for bag in bags:
    while q and q[0][0] <= bag:
        heapq.heappush(tmp, -q[0][1])
        # heapq.heappop(gems)
        q.popleft()
    if tmp:
        item = heapq.heappop(tmp)
        result -= item
print(result)