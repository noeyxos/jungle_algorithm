# 스택
# https://www.acmicpc.net/problem/10828
import sys

n = int(input())
stk = []

for i in range(n):
    task = sys.stdin.readline().split()

    if task[0] == "push":
        stk.append(int(task[1]))
    elif task[0] == "pop":
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif task[0] == "size":
        print(len(stk))
    elif task[0] == "empty":
        if stk:
            print(0)
        else:
            print(1)
    elif task[0] == "top":
        if stk:
            print(stk[-1])
        else:
            print(-1)

