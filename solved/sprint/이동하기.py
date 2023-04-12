def main(n, m, ary):
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            value = ary[i-1][j-1]
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + value
    
    print(dp[n][m])

    
if __name__ == '__main__':
    n, m = map(int, input().split())
    ary = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        ary.append(temp)
    main(n, m, ary)