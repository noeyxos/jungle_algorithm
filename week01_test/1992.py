# 쿼드트리
import sys

def is_same_numbers(x,y, size):
    initial_num = data[x][y]
    # 현재 영역의 모든 칸을 검사하여 같은 숫자인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if data[i][j] != initial_num:
                return False
    return True


def count_numbers(x,y,size):
    if is_same_numbers(x, y, size):
        return str(data[x][y])
    else:
        half_size = size // 2
        top_left = count_numbers(x, y, half_size)
        top_right = count_numbers(x, y + half_size, half_size)
        bottom_left = count_numbers(x + half_size, y, half_size)
        bottom_right = count_numbers(x + half_size, y + half_size, half_size)
        return "(" + top_left + top_right + bottom_left + bottom_right + ")"


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())  # 영상의 크기 입력 받기
    data = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)] # 영상의 숫자 데이터 입력받기

    result = count_numbers(0,0, n) # 데이터에 대해
    print(result)


#
#
# N = int(input())
#
# arr = [list(map(int, input())) for _ in range(N)]
#
#
# def compressor(N, arr):
#     # 영상을 합산 할 변수
#     temp = 0
#     # 영상의 합
#     for lst in arr:
#         temp += sum(lst)
#     # 영상이 모두 1로만 되어 있으면
#     if temp == N ** 2:
#         return '1'
#     # 영상이 모드 0으로만 되어 있으면
#     if temp == 0:
#         return '0'
#     # 0과 1이 섞여있는 경우
#     # 결과는 괄호안에 묶어서
#     result = '('
#     # 왼쪽 위
#     result += compressor(N // 2, [elem[:N // 2] for elem in arr[:N // 2]])
#     # 오른쪽 위
#     result += compressor(N // 2, [elem[N // 2:] for elem in arr[:N // 2]])
#     # 왼쪽 아래
#     result += compressor(N // 2, [elem[:N // 2] for elem in arr[N // 2:]])
#     # 오른쪽 아래
#     result += compressor(N // 2, [elem[N // 2:] for elem in arr[N // 2:]])
#     result += ')'
#
#     return result
#
#
# print(compressor(N, arr))
#
