# (재귀함수) 1부터 n까지 출력하기

n = int(input())

def print_num(n):
    if 1 <= n <= 200:
        if n == 0:
            return
        print(n)
        print_num(n - 1)

# 처음 호출할 때는 1부터 시작
print_num(n)