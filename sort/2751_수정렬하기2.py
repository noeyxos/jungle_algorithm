# 2751번 : 수 정렬하기2
# https://www.acmicpc.net/problem/2751
import sys

n = int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()

for i in li:
    print(i)