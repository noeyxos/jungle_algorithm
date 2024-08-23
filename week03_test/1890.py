# 점프
# https://www.acmicpc.net/problem/1890

# 게임판의 크기
N = int(input())
# 게임 격자판 리스트 만들기
arr = [list(map(int, input().split())) for _ in range(N)] # 점프 크기를 입력


# dp 테이블 생성, 게임 격자판의 크기와 같은 크기 n x n
dp = [[0]*N for _ in range(N)]  #dp[j][j] (i,j)까지 도달할 수 있는 경로의 수
dp[0][0] = 1 # 초기값 세팅

for i in range(N):
    for j in range(N):
        # 현재위치에 도달하는 경로가 있고, 점프할 수 있는 숫자가 있다면,
        if dp[i][j] > 0 and arr[i][j] > 0:
            jump = arr[i][j]    # 현재 위치에서 점프할 수 있는 크기를 jump 라고 저장
            if j+jump < N:        # 범위 내에서 오른쪽으로 점프하기
                dp[i][j+jump] += dp[i][j]
            if i + jump < N:    # 범위 내에서 아래로 쩜프하기
                dp[i+jump][j] += dp[i][j]

print(dp[N-1][N-1])  # dp 크기가 n 이므로 맨 마지막 목표 인덱스 n-1 인 것
   ㅏ# 주의하기..