def main(n):
    dp = [[0] * (10) for _ in range(n+1)]
    dp[1][0] = 0
    for i in range(1, 10):
        dp[1][i] = 1
    if n == 1:
        print(sum(dp[n]))
        return

    for i in range(2, n+1):
        for j in range(10):
            if i == 2 and j == 1:
                dp[i][j] = dp[i-1][j+1]
            elif j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[n]) % 1000000000)


if __name__ == '__main__':
    n = int(input())
    main(n)