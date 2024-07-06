# 2750번: 수 정렬하기
# https://www.acmicpc.net/problem/2750


n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

li = sorted(li)

for i in li:
    print(i)
