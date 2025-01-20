# 블랙잭 
# https://www.acmicpc.net/problem/2798


from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for combi in combinations(cards, 3):
    current_sum = sum(combi)
    if current_sum <= m and current_sum > max_sum:
        max_sum = current_sum

print(max_sum)