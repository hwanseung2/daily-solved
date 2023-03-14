import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return parent

n, m = map(int, input().rstrip().split())
parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i

for _ in range(m):
    cmd, a, b = map(int, input().rstrip().split())
    if cmd == 0:
        parent = union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")