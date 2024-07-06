# 2751번 : 수 정렬하기2
# https://www.acmicpc.net/problem/2751
import sys

n = int(input())
li = []
for i in range(n):
    num = sys.stdin.readline()
    li.append(num)
    li = sorted(li)

for i in li:
    print(i,end="")
