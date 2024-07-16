# 1914번 하노이 탑
# https://www.acmicpc.net/problem/1914

def hanoi_tower(n, start, end) : # n: 원판 갯수 , start: 시작점, end: 끝 점
    if n == 1 :
        print(start, end)
        return

    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계

n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)



# import sys
#
# def hanoi(n, a, b, c):
#     if n == 1:
#         move.append([a, c])
#     else:
#         hanoi(n - 1, a, c, b)
#         move.append([a, c])
#         hanoi(n - 1, b, a, c)
#
#
# move = []
# hanoi(int(sys.stdin.readline()), 1, 2, 3)
# print(len(move))
# print("\n".join([' '.join(str(i) for i in row) for row in move]))