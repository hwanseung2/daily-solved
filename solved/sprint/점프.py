def main(n, ary):
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                print(dp[n-1][n-1])
                return

            jump = ary[i][j]
            ny = i
            nx = j + jump
            if 0 <= ny < n and 0 <= nx < n:
                dp[ny][nx] += dp[i][j]
            ny = i + jump
            nx = j
            if 0 <= ny < n and 0 <= nx < n:
                dp[ny][nx] += dp[i][j]


                


if __name__ == '__main__':
    n = int(input())
    ary = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        ary.append(temp)
    
    main(n, ary)