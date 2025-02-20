# 안전 영역 
# https://www.acmicpc.net/problem/2468

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input()) 
ground = [list(map(int, input().split())) for _ in range(N)]

# 물에 잠기는 높이의 최소값과 최대값 구하기
min_height = min(min(row) for row in ground)
max_height = max(max(row) for row in ground)

# 영역 확인
def is_valid_ground(y, x, height, visited):
    return 0 <= y < N and 0 <= x < N and not visited[y][x] and ground[y][x] > height

# BFS로 안전 영역 확인
def check_ground(start_y, start_x, height, visited):
    q = deque([(start_y, start_x)])
    visited[start_y][start_x] = True

    while q:
        y, x = q.popleft()

        for k in range(4): 
            nxt_y, nxt_x = y + dy[k], x + dx[k]
            if is_valid_ground(nxt_y, nxt_x, height, visited): 
                visited[nxt_y][nxt_x] = True
                q.append((nxt_y, nxt_x))

# 각 높이마다 안전 영역 개수 확인
max_safe_areas = 1 # 비가 오지 않는 경우

for height in range(min_height, max_height):
    visited = [[False] * N for _ in range(N)]
    safe_areas = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and ground[i][j] > height:
                check_ground(i, j, height, visited)
                safe_areas += 1
    
    max_safe_areas = max(max_safe_areas, safe_areas)

print(max_safe_areas)
