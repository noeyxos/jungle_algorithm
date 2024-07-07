# 단어 정렬
# https://www.acmicpc.net/problem/1181


n = int(input())
words = [input() for _ in range(n)]

words = list(set(words))
words.sort()
words.sort(key=lambda i: len(i))
for word in words:
    print(word)