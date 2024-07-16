# 5639 이진 검색 트리
# https://www.acmicpc.net/problem/5639

import sys
input = sys.stdin.readline
#recursion error 방지
sys.setrecursionlimit(10**9) # python3 으로 꼭 바꾸기


# li 안에 있는 값을 비교해본다
# 현재 나보다 작은 애는 왼쪽 / 크면 오른쪾
# 재귀함수를 만들어보자 (종료조건, 콜스택)

def postorder(arr,result):
    if len(arr) == 0:
        return

    left_arr, right_arr = [], []
    root = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > root:
            left_arr = arr[1:i]
            right_arr = arr[i:]
            break
    else:
        left_arr = arr[1:]

    postorder(left_arr, result)
    postorder(right_arr, result)
    result.append(root)

#  이진 검색 트리 입력받기
arr = []
# 입력 끝내기
while True:
    try:
        x = int(input().strip())
        arr.append(x)
    except:
        break

result = []
postorder(arr, result)
print(*result, sep='\n')

# import sys
#
# sys.setrecursionlimit(10 ** 6)
# num_list = []
# while True:
#     try:
#         num = int(input())
#         num_list.append(num)
#     except:
#         break
#
# def postorder(first, end):
#     if first > end:
#         return
#     mid = end + 1  # 루트보다 큰 값이 존재하지 않을 경우를 대비
#     for i in range(first + 1, end + 1):
#         if num_list[first] < num_list[i]:
#             mid = i
#             break
#
#     postorder(first + 1, mid - 1)
#     postorder(mid, end)
#     print(num_list[first])
#
#
# postorder(0, len(num_list) - 1)