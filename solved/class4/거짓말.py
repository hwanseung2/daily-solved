import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
k = list(map(int, input().rstrip().split()))
truth = set() if len(k) == 1 else set(k[1:])
party = []

for _ in range(m):
    temp = list(map(int, input().rstrip().split()))
    participants = set(temp[1:])
    party.append(participants)

for _ in range(m):
    for p in party:
        if len(truth.intersection(p)) > 0:
            truth = truth.union(p)


answer = 0
for p in party:
    if len(p.intersection(truth)) == 0:
        answer += 1

print(answer)
