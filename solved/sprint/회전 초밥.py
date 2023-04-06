import sys
from collections import defaultdict


def main(n, d, k, c, ary):
    set_sushies = defaultdict(int)
    doubling = ary * 2

    start, end = 0, k
    set_sushies[c] += 1
    answer = 0

    for item in doubling[start:end]:
        set_sushies[item] += 1


    while end < (2 * n):
        num = len(set_sushies)
        answer = max(answer, num)

        set_sushies[doubling[end]] += 1
        set_sushies[doubling[start]] -= 1

        if set_sushies[doubling[start]] == 0:
            del set_sushies[doubling[start]]
        
        start += 1
        end +=1
        
    print(answer)


if __name__ == '__main__':
    input = sys.stdin.readline
    n, d, k, c = map(int, input().split())
    ary = []
    for _ in range(n):
        ary.append(int(input()))
    
    main(n, d, k, c, ary)