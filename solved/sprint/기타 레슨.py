import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ary = list(map(int, input().split()))

max_num = max(ary)
start = max_num
end = sum(ary)
answer = int(1e10)

while start <= end:
    mid = (start + end) // 2
    count = 1
    result = 0
    for i in range(n):
        if result + ary[i] <= mid:
            result += ary[i]
        else:
            count += 1
            result = ary[i]

    if count > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
print(answer)