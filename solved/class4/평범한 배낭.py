def main(n, k, ary):
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        weight, value = ary[i-1]
        for j in range(1, k+1):
            if j < weight:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
    print(dp[n][k])

if __name__ == '__main__':
    ary = []
    n, k = map(int, input().split())
    for _ in range(n):
        weight, value = map(int, input().split())
        ary.append((weight, value))
    main(n, k, ary)

