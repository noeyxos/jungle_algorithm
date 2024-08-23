import sys
input = sys.stdin.readline 

def bfs(sj,si,ej,ei):
    # q생성, 필요변수 등 생성
    queue = []
    visited = [0] * store_num

    # 큐에 초기데이터 삽입, si,sj는 v에 표시X
    queue.append((sj,si))

    while queue:
        cj,ci = queue.pop(0)
        if abs(cj-ej) + abs(ci-ei) <= 1000:         # 목적지 도달가능
            return 'happy'

        # 미방문 모든 편의점 좌표: 범위 내 여부 체크
        for i in range(store_num):
            if visited[i] == 0:     # 미방문 편의점
                nj,ni = lst[i]
                if abs(cj-nj)+ abs(ci-ni) <= 1000: # 범위내
                    queue.append((nj,ni))
                    visited[i] = 1

    return 'sad'

test_case = int(input())
for _ in range(test_case):
    store_num = int(input())
    start_j, start_i = map(int, input().split())
    lst = []
    for _ in range(store_num):
        target_j, target_i = map(int, input().split())
        lst.append((target_j,target_i))
    end_j, end_i = map(int, input().split())

    ans = bfs(start_j, start_i, end_j, end_i)
    print(ans)