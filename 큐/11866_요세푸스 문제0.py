# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

from collections import deque

n, k = map(int, input().split())

data = deque(range(1, n+1))
result = []

cnt = len(data)
for i in range(cnt):
    for j in range(k-1):
        temp = data.popleft()
        data += [temp]
    result += [data.popleft()]
print(f"<{', '.join(map(str, result))}>")