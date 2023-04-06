from collections import defaultdict

def solution(gems):
    db = defaultdict(int)
    n = len(gems)
    start, end = 0, 0

    target = set(gems)
    result = []

    # print(targ)
    while end < n and start <= end:
        db[gems[end]] += 1
        set_db = set(db)
        if set_db == target:
            result.append((end-start, start, end))
            db[gems[start]] -= 1
            if db[gems[start]] == 0:
                del db[gems[start]]
            start += 1
        else:
            end += 1

            
        
    result.sort()
    answer = [result[0][1] + 1, result[0][2] + 1]
    return answer
        
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	))
print(solution(["AA", "AB", "AC", "AA", "AC"]	))
print(solution(["XYZ", "XYZ", "XYZ"]	))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	))
    