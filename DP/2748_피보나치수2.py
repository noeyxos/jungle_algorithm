# 피보나치수 2 
# https://www.acmicpc.net/problem/2748


### Top - down 방식

cache = [-1] * 91
cache[0] = 0
cache[1] = 1
 
def f(n): 
    if cache[n] == -1:
      cache[n] = f(n-1) + f(n-2)
    
    return cache[n]

print(f(int(input())))



### Bottom-up 방식

N = int(input())
cache = [-1] * 91
cache[0] = 0
cache[1] = 1
 
for i in range(2, N + 1):
   cache[i] = cache[i - 1] + cache[i - 2]
   
   

print(cache[N])


