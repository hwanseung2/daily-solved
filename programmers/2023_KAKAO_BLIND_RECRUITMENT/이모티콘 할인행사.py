from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    discounts = list(product([40, 30, 20, 10], repeat = len(emoticons)))
    
    for discount in discounts:
        sold = [0, 0]
        for user_dis, user_money in users:
            sold_emoticons = 0
            for emoticon, dis in zip(emoticons, discount):
                if dis >= user_dis:
                    sold_emoticons += emoticon * (1 - dis / 100)
            if sold_emoticons >= user_money:
                sold[0] += 1
            else:
                sold[1] += sold_emoticons
        answer = max(answer, sold)
    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], \
            [1300, 1500, 1600, 4900]))