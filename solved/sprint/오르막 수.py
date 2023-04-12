def main(n):
    dp = [[0] * 10 for _ in range(n+1)]
    for j in range(10):
        dp[1][j] = 1
    if n == 1:
        print(sum(dp[1]))
        return

    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    print(sum(dp[n]) % 10007)
if __name__ == '__main__':
    n = int(input())
    main(n)