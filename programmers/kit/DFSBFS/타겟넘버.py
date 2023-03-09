def check_istarget(numbers, idx, summation, target):
    global answer
    if idx == len(numbers):
        if summation == target:
            answer += 1
        return
    
    num = numbers[idx]
    check_istarget(numbers, idx + 1, summation + num, target)
    check_istarget(numbers, idx + 1, summation - num, target)


def solution(numbers, target):
    global answer
    answer = 0
    check_istarget(numbers, 0, 0, target)
    return answer

print(solution([1,1,1,1,1], 3))
print(solution([4,1,2,1], 4))