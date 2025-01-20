# 나무 자르기
# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline
# 입력 받기
n, m = map(int, input().split())
tree = list(map(int, input().split()))
# 이진 탐색을 위한 변수 초기화
low, high = 0, max(tree)
# 이진 탐색 수행
while low <= high:
    mid = (low + high) // 2
    total = 0
    # mid 높이로 잘랐을 때 얻는 나무 길이 계산
    for t in tree:
        if t > mid:
            total += t - mid
    # 필요한 길이와 비교하여 범위 조정
    if total < m:
        high = mid - 1
    else:
        low = mid + 1
# 정답 출력
print(high)