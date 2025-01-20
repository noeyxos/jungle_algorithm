# 2606 바이러스  https://www.acmicpc.net/problem/2606



def dfs(c):
    global ans
    v[c]=1
    ans+=1

    for n in arr[c]:
        if not v[n]:
            dfs(n)

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)
v = [0]*(N+1)
ans = 0
dfs(1)
print(ans-1)