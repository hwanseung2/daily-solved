def main(N, M, memory, cost):
    cost_sum = sum(cost)
    dp = [[0] * (cost_sum + 1) for _ in range(N+1)]

    for i in range(1, N+1):
        m, c = memory[i-1], cost[i-1]
        for j in range(cost_sum+1):
            if j < c:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + m)
    
    for j in range(cost_sum + 1):
        for i in range(N+1):
            if dp[i][j] >= M:
                return j

if __name__ == '__main__':
    N, M = map(int, input().split())
    memory = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    print(main(N, M, memory, cost))