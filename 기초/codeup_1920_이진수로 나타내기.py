# 이진수로 나타내기
def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)


n = int(input())
if n == 0:
    print(0)
else:
    print(to_binary(n))