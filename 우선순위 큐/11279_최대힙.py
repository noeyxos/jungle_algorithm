# 최대 힙
# https://www.acmicpc.net/problem/11279

import heapq
import sys

max_heap = []
x = 0
n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if x > 0 :
        heapq.heappush(max_heap, -x)
    elif x == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(-(heapq.heappop(max_heap)))