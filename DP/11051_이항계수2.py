# 이항계수2 
# https://www.acmicpc.net/problem/11051


### Top-down 형식으로 풀기

import sys

MOD = 10007
sys.setrecursionlimit(10 ** 7)

cache = [[0]* 1001 for _ in range(1001)]
N, K = map(int, input().split())

def bino(n, k):
    if cache[n][k] : 
        return cache[n][k]

    if k == 0 or k == n : 
        cache[n][k] = 1
    else: 
        cache[n][k] = bino(n-1, k-1) + bino(n-1, k)
        cache[n][k] %= MOD
    
    return cache[n][k]
    



print(bino(N, K))


### Bottom - up 형식으로 풀기

import sys

MOD = 10007


cache = [[0]* 1001 for _ in range(1001)]
N, K = map(int, input().split())

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i): 
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD

print(cache[N][K])