import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ary = list(map(int, input().split()))

start = 0
# end = int(2e10)
end = max(ary)

while start <= end:
    mid = (start + end) // 2

    result = 0
    for i in range(n):
        if ary[i] > mid:
            result += (ary[i] - mid)

    if result < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
print(answer)
