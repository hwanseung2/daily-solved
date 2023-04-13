import sys
input = sys.stdin.readline

def main(n, m, ary):
    start = 1
    end = int(1e20)
    answer = end
    
    while start <= end:
        mid = (start + end) // 2 # 심사에 마치는 시간
        
        result = 0
        for i in range(n):
            result += mid // ary[i]
        if result >= m:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    print(answer)
            

if __name__ == '__main__':    
    n, m = map(int, input().split())
    ary = [int(input()) for _ in range(n)]
    main(n, m, ary)