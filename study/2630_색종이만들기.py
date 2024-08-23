# 색종이 만들기
# https://www.acmicpc.net/problem/2630
import sys
input = sys.stdin.readline


# 색깔 확인
def same_color(i, j, length):
    global  white, blue
    same_color = True
    start_color = color_paper[0][0]
    current_color = color_paper[j][i]
    for _ in range(length):
        if start_color == current_color:
            if current_color == 0:
                white += 1
            else:
                blue += 1
        else:
            same_color = False
    return same_color


# 종이 자르기
def cut_paper(i, j, length):
    # 모두 1인지 0인지 확인
    start_point = color_paper[0][0]
    current_point = color_paper[j][i]
    N = k//2
    # 1사분면 어쩌고 하는게 있었는데 기억이 안난ㄷ..






# 전체 종이의 한 변의 길이
n = int(input())

color_paper = [list(map(int,input().split())) for _ in range(n)]

white, blue = 0, 0

print(white)
print(blue)