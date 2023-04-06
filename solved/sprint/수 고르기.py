INF = int(3e10)
def main(n, m, ary):
    ary.sort()
    start, end = 0, 1
    answer = INF

    while end < n and start <= end:
        target = ary[end] - ary[start]
        if target >= m and target <= answer:
            answer = target
        if target > m:
            start += 1
        elif target < m:
            end += 1
        else:
            break
    print(answer)
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    ary = []
    for _ in range(n):
        ary.append(int(input()))
    
    main(n, m, ary)