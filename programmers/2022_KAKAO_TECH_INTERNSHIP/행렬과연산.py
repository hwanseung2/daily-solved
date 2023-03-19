from collections import deque

# def shiftrow(matrix, n, m):
#     matrix.appendleft(matrix.pop())
#     return matrix

# def rotate(matrix, n, m):
#     new_matrix = [[0] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if i == 0 and (j >= 0 and j <= m-2):
#                 new_matrix[i][j+1] = matrix[i][j]
#             elif i == n-1 and (j >= 1 and j <= m-1):
#                 new_matrix[i][j-1] = matrix[i][j]
#             elif (i >= 1 and i <= n-1) and j == 0:
#                 new_matrix[i-1][j] = matrix[i][j]
#             elif (i >= 0 and i <= n-2) and j == m-1:
#                 new_matrix[i+1][j] = matrix[i][j]
#             else:
#                 new_matrix[i][j] = matrix[i][j]
#     new_matrix = deque(new_matrix)
#     return new_matrix


# def solution(rc, operations):
#     answer = [[]]
#     n = len(rc)
#     m = len(rc[0])
    
#     rc = deque(rc)

#     ops = "".join(operations)
#     while "ShiftRow" in ops:
#         ops = ops.replace("ShiftRow", "S")
#     while "Rotate" in ops:
#         ops = ops.replace("Rotate", "R")
#     i_s = "S" * n
#     i_r = "R" * (2*n + 2*m - 4)

#     while i_s in ops:
#         ops = ops.replace(i_s, "I")
#     while i_r in ops:
#         ops = ops.replace(i_r, "I")

#     for op in ops:
#         if op == "R":
#             rc = rotate(rc, n, m)
#         elif op == "S":
#             rc = shiftrow(rc, n, m)
#         else:
#             continue
#     answer = list(rc)
#     return answer

from collections import deque

def solution(rc, operations):
    n, m = len(rc), len(rc[0])
    rows = deque(deque(row[1:-1]) for row in rc)
    out_cols = [deque(rc[r][0] for r in range(n)), deque(rc[r][m-1] for r in range(n))]

    for operation in operations:
        if operation[0] == "S":
            rows.appendleft(rows.pop())
            out_cols[0].appendleft(out_cols[0].pop())
            out_cols[1].appendleft(out_cols[1].pop())
        
        else:
            rows[n-1].append(out_cols[1].pop())
            out_cols[0].append(rows[n-1].popleft())
            rows[0].appendleft(out_cols[0].popleft())
            out_cols[1].appendleft(rows[0].pop())
    
    answer = []
    for i in range(n):
        answer.append([])
        answer[i].append(out_cols[0][i])
        answer[i].extend(rows[i])
        answer[i].append(out_cols[1][i])
    return answer


# print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["Rotate", "ShiftRow"]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]	, ["Rotate", "ShiftRow"]	))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]]	, ["Rotate", "ShiftRow", "ShiftRow"]	))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]	,["ShiftRow", "Rotate", "ShiftRow", "Rotate"]	))