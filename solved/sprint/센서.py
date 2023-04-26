import sys

input = sys.stdin.readline

def main(n, m, ary):
    ary.sort()
    diff = []
    for i in range(1, n):
        diff.append(ary[i] - ary[i-1])
    diff.sort(key = lambda x: -x)
    print(sum(diff[k-1:]))

if __name__ == '__main__':
    n = int(input().rstrip())
    k = int(input().rstrip())
    ary = list(map(int, input().split()))
    main(n, k, ary)