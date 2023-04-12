import sys
input = sys.stdin.readline

n = int(input().rstrip())
ary = list(map(int, input().split()))
T = int(input().rstrip())

dp = [0] * n
dp[0] = ary[0]
for i in range(1, n):
    dp[i] = dp[i-1] + ary[i]

for _ in range(T):
    start, end = map(int, input().split())
    start -= 1
    end -= 1

    print(dp[end] - dp[start] + ary[start])