# 수 찾기
# https://www.acmicpc.net/problem/1920

# set으로 풀기
# import sys

# n = int(input())
# nl = set(map(int, sys.stdin.readline().split()))
# m = int(input())
# ml = list(map(int, sys.stdin.readline().split()))
#
# for x in ml:
#     if x in nl:
#         print(1)
#     else:
#         print(0)


# 이분 탐색으로 풀기
def bin_search(arr, target):
    pl = 0
    pr = len(arr) - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        if arr[pc] == target:
            return pc
        elif arr[pc] < target:
            pl = pc + 1
        else:
            pr = pc - 1
    return -1

n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))

# 미리 nl을 정렬
nl.sort()

for key in ml:
    idx = bin_search(nl, key)
    if idx != -1:
        print(1)
    else:
        print(0)