# 수 찾기
# https://www.acmicpc.net/problem/1920

import sys

n = int(input())
nl = set(map(int, sys.stdin.readline().split()))
m = int(input())
ml = list(map(int, sys.stdin.readline().split()))

for x in ml:
    if x in nl:
        print(1)
    else:
        print(0)