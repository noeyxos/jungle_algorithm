# 외판원 순회 2
# https://www.acmicpc.net/problem/10971

n = int(input())
w = [[*map(int, input().split())] for _ in range(n)]  # n행 배열 입력 받는 법

min_cost = 1e9 # 최솟값 셋팅 - 초기는 매우 큰 값으로
visited = [False for _ in range(n)] # 방문 여부
temp = list() #현재 방문 경로를 지정하는 리스트

def go(depth, cost) -> int: # 재귀함수 (depth = 현재 탐색 깊이 , cost = 비용)
    global min_cost

    if cost >= min_cost: return # 기저조건 (1)_(현재 비용이 최소비용보다 크거나 같다면 탐색하지 않음)

    if depth == n: # 기저 조건 (2) 모든 도시를 방문했다면, 출발도시로 돌아오는 비용을 추가하여 min_cost 갱신
        if w[temp[n-1]][temp[0]] != 0:
        # print(f'{next} to {start} : {distance} + {w[next][start]}')
        # print(f"distance = {distance}")
            min_cost = min(min_cost, cost + w[temp[-1]][temp[0]])  # 최솟값 갱신
        return

    for i in range(n):
        if depth == 0 or (visited[i] == False and w[temp[depth-1]][i] != 0) : # 첫번째 도시는 무조건 방문, 그 이후에는 방문하지 않은 도시 중에서 갈 수 있는 경우만 방문
            temp.append(i) # 현재 도시를 방문 경로에 추가
            visited[i] = True # 방문 체크

            go(depth + 1, cost + w[temp[depth-1]][i]) # 재귀 호출 다음 도시 탐색

            temp.pop() # 현재 도시를 방문 경로에서 제거
            visited[i] = False # 현재 도시의 방문을 해제


    return


go(0,0)
print(min_cost)