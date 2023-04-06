def main(n, m, ary):
    start, end = 0, 1
    answer = 0
    while end <= n and start <= end:
        num = sum(ary[start:end])
        if num < m:
            end +=1
        elif num > m:
            start += 1
        else:
            answer += 1
            end += 1
    print(answer)

if __name__ == "__main__":
    n, m = map(int, input().split())
    ary = list(map(int, input().split()))
    main(n, m, ary)