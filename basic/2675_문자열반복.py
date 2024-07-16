# 문자열 반복
# https://www.acmicpc.net/problem/2675


t = int(input())

for _ in range(t):
    r, s = input().split()
    text =''
    for i in s:
        text += int(r)*i
    print(text)