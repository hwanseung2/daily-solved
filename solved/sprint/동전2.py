def main(n, k, ary):
    dp = [10001] * (k+1)
    dp[0] = 0

    for i in range(n):
        value = ary[i]
        for j in range(value, k+1):
            dp[j] = min(dp[j], dp[j - value]+1)
    

    answer = dp[k]
    if answer == 10001:
        print(-1)
    else:
        print(answer)

if __name__ == '__main__':
    n, k = map(int, input().split())
    ary = [int(input()) for _ in range(n)]
    main(n, k, ary)