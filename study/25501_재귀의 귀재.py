# 재귀의 귀재
# https://www.acmicpc.net/problem/25501

def recursion(word, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif word[l] != word[r]:
        return 0
    else:
        return recursion(word, l + 1, r - 1)


def is_palindrom(word):
    return recursion(word, 0, len(word) - 1)

test_case = int(input())

for _ in range(test_case):
    string = input().strip()
    cnt = 0
    result = is_palindrom(string)
    print(result, cnt)