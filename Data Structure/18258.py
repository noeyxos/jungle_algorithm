# 큐2
# https://www.acmicpc.net/problem/18258
from collections import deque
import sys

n = int(input())
queue = deque()

for _ in range(n):
    task = sys.stdin.readline().split()
    if task[0] == "push":
        queue.append(int(task[1]))
    elif task[0] == "pop":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif task[0] == "size":
        print(len(queue))
    elif task[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif task[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif task[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)