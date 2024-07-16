# 괄호의 값
# https://www.acmicpc.net/problem/2504

stk = []
result = 0
temp = 1

li = list(input())

for i in range(len(li)):
    if li[i] == "(":
        temp *= 2
        stk.append(li[i])
    elif li[i] == "[":
        temp *= 3
        stk.append(li[i])

    elif li[i] == ")":
        if not stk or stk[-1] != "(":
            result = 0
            break
        if li[i - 1] == "(":
            result += temp
        stk.pop()
        temp //= 2

    elif li[i] == "]":
        if not stk or stk[-1] != "[":
            result = 0
            break
        if li[i - 1] == "[":
            result += temp
        stk.pop()
        temp //= 3

if stk:
    print(0)
else:
    print(result)