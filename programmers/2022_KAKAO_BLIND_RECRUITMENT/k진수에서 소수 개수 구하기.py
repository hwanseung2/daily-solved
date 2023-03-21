import math

def divide_k(n, k):
    string = ''
    while n != 0:
        res = n % k
        n = n // k
        string += str(res)
    string = string[::-1]
    return string

def is_prime(x):
    if len(x) == 0:
        return False
    x = int(x)
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True


def solution(n, k):
    answer = 0
    string = divide_k(n, k)
    candidates = string.split('0')
    for cand in candidates:
        if is_prime(cand):
            answer += 1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))