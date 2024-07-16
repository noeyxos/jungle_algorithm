# 홀수 찾기

# def odd(a, b):
#     # 종료조건
#     global row
#     if a > b:
#         return
#     # 콜함수
#     if a % 2 != 0:
#         row.append(a)
#     return odd(a + 1, b)
# a, b = map(int, input().split())
# row = []
# odd(a, b)
# print(*row)


def odd(a, b):
    global temp
    if a == 1 and b == 1:
        print(1)
    if a == b or a > b:
        return
    if a % 2 == 1:
        temp.append(a)
        print(a, end=' ')
    else:
        temp.append(a + 1)
        print(a + 1, end=' ')
    odd(a + 2, b)


a, b = map(int, input().split())
temp = []
odd(a, b)