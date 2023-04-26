import sys
from collections import defaultdict
input = sys.stdin.readline

def main(n, m, crane, boxes):
    crane_dict = defaultdict(list)
    crane_idx = defaultdict(int)
    box_list = []
    visited = [False] * m
    cnt = m
    answer = 0

    for i, box in enumerate(boxes):
        box_list.append((box, i))
    
    for item in box_list:
        for i in range(n):
            if crane[i] >= item[0]:
                crane_dict[crane[i]].append(item)
    
    for c in crane:
        crane_dict[c].sort(key = lambda x: (-x[0], x[1]))
    
    while cnt > 0:
        answer += 1
        for c in crane:
            if len(crane_dict[c]) == 0:
                continue
            if cnt <= 0:
                return answer
            flag = False
            while flag == False:
                if crane_idx[c] >= len(crane_dict[c]):
                    break
                process = crane_dict[c][crane_idx[c]]
                if visited[process[1]] == False:
                    visited[process[1]] = True
                    cnt -= 1
                    crane_idx[c] += 1
                    flag = True
                else:
                    crane_idx[c] += 1
    
    return answer
    

if __name__ == '__main__':
    n = int(input().rstrip())
    crane = list(map(int, input().split()))
    m = int(input().rstrip())
    box = list(map(int, input().split()))

    if max(box) > max(crane):
        print(-1)
    else:
        print(main(n, m, crane, box))