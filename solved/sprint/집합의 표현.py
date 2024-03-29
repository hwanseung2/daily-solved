import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, T = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
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

for _ in range(T):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        parent = union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")