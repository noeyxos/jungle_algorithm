# 7569번 토마토 https://www.acmicpc.net/problem/7569

import sys 

def bfs():
    # [1] q:생성, v[]:생성
    q = []
    v = [[[0] * M for _ in range(N)]for _ in range(M)]

    # [2] q에 초기데이터(를) 삽입. 안익은 토마토 카운트 
    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    q.append(h, i, j)
                    v[h][i][j] = 1
                elif arr[h][i][j] == 0:
                    cnt +=1 

    while q:
        ch, ci, cj = q.pop(0)
        



M,N,H = map(int, input().split())
arr = [[list(map(int, input.split())) for _ in range(M)]]
ans = bfs()
print(ans)
