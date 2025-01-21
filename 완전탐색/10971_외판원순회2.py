# 외판원 순회2 
# https://www.acmicpc.net/problem/10971

import sys

n = int(input())
routes = [list(map(int, input().split())) for _  in range(n)]

min_route = sys.maxsize # 최소 비용 초기값을 큰 값으로 설정

def get_route(route, visited, cur_idx, first_idx): #이동비용, 방문여부, 현재위치, 출발위치
    global min_route

    # 모든 도시를 방문했다면
    if all(visited): 
        if routes[cur_idx][first_idx] != 0: # 출발점으로 돌아갈 수 있다면
            min_route = min(min_route, route + routes[cur_idx][first_idx])
        return 
    for i in range(n):
        if not visited[i] and routes[cur_idx][i] != 0: # 방문하지 않았고, 비용이 0이 아닌 곳 
            visited[i] = True 
            get_route(route + routes[cur_idx][i], visited, i, first_idx) # 다음 도시로 이동 
            visited[i] = False # 다시 방문하지 않은 상태로 되돌림
    
for i in range(n) : 
    visited = [False] * n
    visited[i] = True
    get_route(0, visited, i, i)

print(min_route)