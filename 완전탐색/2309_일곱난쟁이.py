# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

from itertools import combinations

heights = [int(input()) for _ in range(9)]
for combi in (combinations(heights, 7)):
    if sum(combi) == 100 :
        for height in sorted(combi):
            print(height)
        break


## 또 다른 풀이 
heights = [int(input()) for _ in range(9)]
heights.sort()
tot = sum(heights)
for i in range(8):
    for j in range(i + 1, 9):
        if tot - heights[i] - heights[j] == 100:
            for k in range(9):
                if i != k and j != k :
                    print(heights[k])
            break
