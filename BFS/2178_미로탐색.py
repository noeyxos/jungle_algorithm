# 미로탐색 
# https://www.acmicpc.net/problem/2178

from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs():
    q = deque([(0, 0)])

    while q:
        y, x = q.popleft()


        if y == n - 1 and x == m - 1:
            return graph[y][x]
        

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1 
                q.append((ny, nx))

    return -1

print(bfs())