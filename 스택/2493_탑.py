# 탑
# https://www.acmicpc.net/problem/2493

import sys

n = int(input())
tops = list(map(int, sys.stdin.readline().split()))

result = [0] * n
stk = []

for i in range(n):
    while stk and tops[stk[-1]] <= tops[i]:
        stk.pop()
    if stk:
        result[i] = stk[-1] + 1
    stk.append(i)

print(' '.join(map(str, result)))