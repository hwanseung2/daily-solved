import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ary = list(map(int, input().split()))

max_num = max(ary)
min_num = min(ary)

start = 0
end = max_num - min_num

while start <= end:
    mid = (start + end) // 2 #구간의 점수가 가질 수 있는 최대의 값

    count = 1
    max_temp = 0
    min_temp = 10001
    for i in range(n):
        max_temp = max(max_temp, ary[i])
        min_temp = min(min_temp, ary[i])
        if max_temp - min_temp > mid:
            count += 1
            max_temp = ary[i]
            min_temp = ary[i]
    if count <= m:
        end = mid - 1 
        answer = mid
    elif count > m:
        start = mid + 1

print(answer)
