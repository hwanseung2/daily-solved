from collections import defaultdict

#TODO: 날짜 다루는 문제. privacy에서 약관을 더해서 today보다 큰 지 작은 지를 판단
#TODO: 비교할 때는 y부터
#TODO: terms는 dict로 바로 매칭. key는 유일

def convert_day2int(day):
    y, m, d = day.split('.')
    y, m, d = int(y), int(m), int(d)
    return (y, m, d)

def add_term(item, day):
    y, m, d = day
    temp_y, temp_m = divmod(m + item, 12)
    y += temp_y
    m = temp_m

    d = d - 1
    if d == 0:
        m -= 1
        d = 28
    if m == 0:
        y -= 1
        m = 12
    
    return (y, m, d)
    

def compare_day(anchor, compare):
    anc_y, anc_m, anc_d = anchor
    com_y, com_m, com_d = compare

    if com_y < anc_y:
        return True
    if com_y == anc_y and com_m < anc_m:
        return True
    if com_y == anc_y and com_m == anc_m and com_d < anc_d:
        return True
    
    return False



def solution(today, terms, privacies):
    answer = []
    db = defaultdict(int)
    for term in terms:
        key_, item_ = term.split()
        item_ = int(item_)
        db[key_] = item_

    today = convert_day2int(today)
    for idx, privacy in enumerate(privacies):
        day, key_ = privacy.split()
        item = db[key_]
        day = convert_day2int(day)
        day = add_term(item, day)
        if compare_day(today, day):
            answer.append(idx + 1)

    return answer

# print(add_term(3, (2021, 12, 1)))
print(solution("2022.05.19"	, ["A 6", "B 12", "C 3"]	, ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	))
print(solution("2020.01.01"	, ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]	))

def convert_day2int(day):
    y, m, d = day.split('.')
    return int(y)*12*28 + int(m)*28 + int(d)

def solution(today, terms, privacies):
    answer = []
    db = defaultdict(int)
    for term in terms:
        key, item = term.split()
        db[key] = int(item)
    
    for idx, privacy in enumerate(privacies):
        day, key = privacy.split()
        add_term = db[key] * 28
        if convert_day2int(day) + add_term <= convert_day2int(today):
            answer.append(idx + 1)

    return answer

print(solution("2022.05.19"	, ["A 6", "B 12", "C 3"]	, ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	))
print(solution("2020.01.01"	, ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]	))
