# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309
import sys
from functools import reduce
from itertools import combinations

# 9명의 난쟁이 등장
workers = [int(sys.stdin.readline()) for _ in range(9)]

for combination in combinations(workers,7):
    if reduce(lambda x, y: x + y, combination) == 100:
        result = sorted(combination)
        print('\n'.join(map(str, result)))
        break