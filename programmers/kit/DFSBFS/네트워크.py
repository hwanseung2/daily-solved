def check_network(computers, n, i):
    global visited

    for j in range(n):
        if computers[i][j] == 1 and visited[j] != True:
            visited[j] = True
            check_network(computers, n, j)


def solution(n, computers):
    global visited
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] != True:
            visited[i] = True
            answer += 1
            check_network(computers, n, i)
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))