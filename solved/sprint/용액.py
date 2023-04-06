INF = int(1e10)

def main(n, ary):
    answer = INF
    start, end = 0, n-1
    while start < end:
        num = ary[start] + ary[end]
        if abs(num) <= answer:
            ans_start = start
            ans_end = end
            answer = abs(num)
        if num > 0:
            end -= 1
        elif num < 0:
            start += 1
        else:
            break
    print(ary[ans_start], ary[ans_end])

if __name__ == '__main__':
    n = int(input())
    ary = list(map(int, input().split()))
    
    main(n, ary)