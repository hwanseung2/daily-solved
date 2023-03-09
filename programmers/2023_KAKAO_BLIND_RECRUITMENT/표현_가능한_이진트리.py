import math


def make_binary(number):
    binary_num = bin(number)[2:]
    max_len = 2 ** (int(math.log(len(binary_num), 2)) + 1) - 1
    binary_num = binary_num.zfill(max_len)
    return binary_num

def check_tree(binary_num):
    if len(binary_num) == 1:
        return True
    mid = len(binary_num) // 2
    if binary_num[mid] == '1':
        return check_tree(binary_num[:mid]) and check_tree(binary_num[mid+1:])
    else:
        return sum(map(int, list(binary_num))) == 0

def solution(numbers):
    answer = []
    for number in numbers:
        binary_num = make_binary(number)
        if check_tree(binary_num):
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([7, 42, 5]))
print(solution([63, 111, 95]))