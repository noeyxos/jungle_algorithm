# 11725 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

from sys import setrecursionlimit, stdin
input = stdin.read # 모든 입력을 한번에 읽기
setrecursionlimit(100000)  # 파이썬 재귀 한도를 늘려주는 함수

# Read all input data
data = input().split()

# Parse the number of nodes
n = int(data[0]) # 노드의 수 n

# Adjacency list
adj = [[] for _ in range(n + 1)] # adj : 인접리스트, 각 노드의 인접 노드들을 저장

# Parent array
p = [0] * (n + 1) # p : 각 노드의 부모 노드를 저장 , 처음에는 모두 0으로 초기화

# 인접 리스트 구성
index = 1
for _ in range(n - 1):
    u = int(data[index])
    v = int(data[index + 1])
    adj[u].append(v)
    adj[v].append(u)
    index += 2

def dfs(cur):
    for nxt in adj[cur]:
        if p[cur] == nxt:
            continue
        p[nxt] = cur
        dfs(nxt)

# Perform DFS starting from node 1
dfs(1)

# Print the parent of each node starting from node 2 to n
for i in range(2, n + 1):
    print(p[i])

#
#
# import sys
# from collections import deque
#
# N = int(sys.stdin.readline())
# graph = [[] for i in range(N+1)]
# for _ in range(N-1):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# queue = deque()
# queue.append(1)
#
# ans = [0]*(N+1)
#
# def bfs():
#     while queue:
#         now = queue.popleft()
#         for nxt in graph[now]:
#             if ans[nxt] == 0:
#                 ans[nxt] = now
#                 queue.append(nxt)
#
# bfs()
# res = ans[2:]
# for x in res:
#     print(x)