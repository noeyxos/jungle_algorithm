# # 피보나치 함수
# # https://www.acmicpc.net/problem/1003
# import sys
# input = sys.stdin.readline
#
# test_case = int(input())
#
# max_n = 40
# dp = [(0,0)] * (max_n + 1)
#
# dp[0] = (1,0)
# dp[1] = (0,1)
#
# def fibo(n):
#     zero_cnt, one_cnt = 0, 0
#
#     if n  == 0:
#         zero_cnt += 1
#         return 0
#     elif n == 1:
#         one_cnt += 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# for _ in range(test_case):
#     test = int(input())
#     print(fibo(test))


import sys
input = sys.stdin.readline

test_case = int(input())

# 최대 피보나치 수를 저장할 배열 크기 설정
max_n = 40
dp = [(0, 0)] * (max_n + 1)

# 초기 값 설정
dp[0] = (1, 0)  # fibo(0)을 호출할 때 (0을 출력하는 횟수, 1을 출력하는 횟수)
dp[1] = (0, 1)  # fibo(1)을 호출할 때 (0을 출력하는 횟수, 1을 출력하는 횟수)

# 동적 프로그래밍으로 미리 계산
for i in range(2, max_n + 1):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

# 테스트 케이스 처리
for _ in range(test_case):
    test = int(input())
    print(dp[test][0], dp[test][1])