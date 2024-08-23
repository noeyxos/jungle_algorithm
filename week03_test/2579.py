# 계단 오르기
# https://www.acmicpc.net/problem/2579

import sys
input = sys.stdin.readline

# 계단의 개수
stair_num = int(input())
# 각 계단의 점수 저장
stair_point = [0] + [int(input()) for _ in range(stair_num)] # 인덱스 1부터 시작

# dp 테이블 생성 및 초기화
dp = [[0]*3 for _ in range(stair_num+1)] # n x 3 크기의 테이블 생성, dp[i][] : i번째 계단 밟았을 때의 최댓값 저장

for i in range(1, stair_num+1):
    dp[i][0] = max(dp[i-1][1], dp[i -1][2]) # 현재 위치를 안 밟는 경우
    dp[i][1] = dp[i-1][0] + stair_point[i] # 직전 칸을 밟지 않고 현재 칸 밟기
    dp[i][2] = dp[i - 1][1] + stair_point[i] # 직전 칸을 밟고 현재 칸 밟기

print(max(dp[stair_num][1], dp[stair_num][2]))