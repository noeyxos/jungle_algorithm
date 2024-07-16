# 최소 스패닝(신장) 트리
# https://www.acmicpc.net/problem/1197

# 크루스칼 알고리즘

import sys

input = sys.stdin.readline

v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화
for i in range(1, v + 1):  # 각 정점의 부모를 자신으로 설정
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:  # x가 자기 자신이 아니라면
        parent[x] = find_parent(parent, parent[x])  # 해당 x로 다시 함수 호출(재귀)
    return parent[x]

def union_parent(parent, a, b):  # 두 원소가 속한 집합을 합침
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a  # b의 부모를 a가 한다.
    else:
        parent[a] = b  # a의 부모를 b가 한다.

edges = []
total_cost = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 정렬은 한 번만 수행
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)

#######################################################
# 프림 알고리즘
import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

# 인접 리스트를 이용해 그래프 표현
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

def prim(start):
    visited = [False] * (v + 1)
    min_heap = [(0, start)]  # (cost, vertex)
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost

        for edge_cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_cost, v))

    return total_cost

# 임의의 시작점 1에서 시작
print(prim(1))