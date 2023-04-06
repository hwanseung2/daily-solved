n, k = map(int, input().split())

values = []
weights = []
for _ in range(n):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

bag_values = values.copy()
bag_weights = weights.copy()

for i in range(n):
    for j in range(i):
        if bag_weights[j] + weights[i] <= k:
            if bag_values[i] < bag_values[j] + values[i]:
                bag_weights[i] = bag_weights[j] + weights[i]
                bag_values[i] = bag_values[j] + values[i]

print(max(bag_values))

def knapsack(N, K, items):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        weight, value = items[i - 1]
        for j in range(K + 1):
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    return dp[N][K]


def main():
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    result = knapsack(N, K, items)
    print(result)


if __name__ == "__main__":
    main()
