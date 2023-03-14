# import sys
# from collections import defaultdict

# sys.setrecursionlimit(int(1e6))
# input = sys.stdin.readline

# def check_small(a, b):
#     length_a = len(a)
#     length_b = len(b)
#     if length_a < length_b:
#         return a
#     elif length_a > length_b:
#         return b
#     else:
#         min_length = min(length_a, length_b)
#         for i in range(min_length):
#             if ord(a[i]) < ord(b[i]):
#                 return a
#             elif ord(a[i]) > ord(b[i]):
#                 return b
#     return a

# def find_parent(network, x):
#     if network[x] != x:
#         network[x] = find_parent(network, network[x])
#     return network[x]

# def union_parent(network, a, b):
#     a = find_parent(network, a)
#     b = find_parent(network, b)

#     check_small_name = check_small(a, b)
#     if check_small_name == a:
#         network[b] = a
#     else:
#         network[a] = b

#     return network, check_small_name


# T = int(input().rstrip())
# for _ in range(T):
#     F = int(input().rstrip())
#     network = defaultdict(str)
#     for _ in range(F):
#         a, b = input().rstrip().split()
#         if network.get(a) == None:
#             network[a] = a
#         if network.get(b) == None:
#             network[b] = b

#         network, name = union_parent(network, a, b)
#         root_name = find_parent(network, name)
#         cnt = 0
#         for key, value in network.items():
#             if find_parent(network, key) == root_name:
#                 cnt += 1
#         print(cnt)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]

T = int(input())
for _ in range(T):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x, y)
        print(number[find(x)])

