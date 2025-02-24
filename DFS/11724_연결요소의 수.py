# 연결 요소의 개수 
# https://www.acmicpc.net/problem/11724


N, M = map(int, input().split())

gragh = [[] for _ in range(N+1)]

for _ in range(M) :
    a , b = map(int, input().split())
    gragh[a].append(b)
    gragh[b].append(a)

visited = [False] * (N + 1)

def dfs(graph, v, visited):
    visited[v] = True

    for i in gragh[v]:
        if not visited[i]:
            dfs(graph, i, visited)


count = 0 
for i in range(1, N +1):
    if not visited[i]:
        dfs(gragh, i, visited)
        count += 1
print(count)
