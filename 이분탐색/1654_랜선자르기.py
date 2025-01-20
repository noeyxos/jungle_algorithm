# 랜선자르기
# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = []
for _ in range(n):
    li.append(int(input()))

# 최소, 최대 길이 설정
min_size = 1
max_size = max(li)

while min_size <= max_size:
    mid_size = (min_size + max_size) // 2 # 중간값 구하기
    lan = 0
    for i in li:
        lan += i // mid_size
    if lan >= k :
        min_size = mid_size + 1
    else:
        max_size = mid_size - 1

print(max_size)