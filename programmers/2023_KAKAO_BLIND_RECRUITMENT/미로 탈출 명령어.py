import sys
sys.setrecursionlimit(5000)
dy = [1, 0, 0, -1]
dx = [0, -1, 1, 0]
direc = ['d', 'l', 'r', 'u']

def l1_norm(y, x, r, c):
    norm = abs(y - r) + abs(x - c)
    return norm

def dfs(n, m, y, x, r, c, k, cnt, tracked):
    global answer, flag
    dist = l1_norm(y, x, r, c)
    if flag == True:
        return
    if dist > (k - cnt) or (k-cnt) % 2 != dist % 2:
        return
    
    if flag == False and cnt == k and y == r and x == c:
        answer = ''.join(tracked)
        flag = True
        return
    elif cnt > k:
        return
    else:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 1 or nx < 1 or ny > n or nx > m:
                continue
            dfs(n, m, ny, nx, r, c, k, cnt + 1, tracked + [direc[i]])


def solution(n, m, x, y, r, c, k):
    global answer, flag
    answer = ''
    flag = False
    dfs(n, m, x, y, r, c, k, 0, [])
    if flag == False:
        return 'impossible'
    else:
        return answer

print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))