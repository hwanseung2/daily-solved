def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    check_d = 0
    check_p = 0
    for i in range(n):
        check_d += deliveries[i]
        check_p += pickups[i]

        while check_d > 0 or check_p > 0:
            check_d -= cap
            check_p -= cap
            answer += (n - i) * 2
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))