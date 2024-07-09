# 뱀
# https://www.acmicpc.net/problem/3190

n = int(input())
li = [[0] * n for _ in range(n)]

k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    li[a][b] = 1

l = int(input())
for j in range(l):
    x, c = map(input().split())
    # if c =="L":
    # elif c == "R":