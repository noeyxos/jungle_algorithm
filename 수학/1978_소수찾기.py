# 소수 찾기
# https://www.acmicpc.net/problem/1978

n = int(input())
count = 0
number = map(int,input().split())

for num in number:
    if num == 1:
        count += 1
        continue
    for i in range(2, num):
        if num % i == 0:
            count += 1
            break
print(n-count)
