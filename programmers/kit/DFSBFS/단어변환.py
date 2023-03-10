from collections import deque

def solution(begin, target, words):
    queue = deque([])
    words_length = len(words)
    visited = [False] * words_length
    queue.append((begin, 0))
    if begin in words:
        idx = words.index(begin)
        visited[idx] = True

    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        for i in range(words_length):
            candidate = words[i]
            word_count = 0
            for j in range(len(word)):
                if word[j] != candidate[j]:
                    word_count += 1

            if visited[i] == False and word_count == 1:
                visited[i] = True
                queue.append((candidate, cnt + 1))

    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(solution("aab", "aba", ["abb", "aba"]))