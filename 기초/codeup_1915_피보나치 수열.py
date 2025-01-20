# 피보나치 수열
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)
#
# num = int(input())
# print(fibo(num))

nacci = [1, 1]
def fibo(n):
    global nacci
    if n == 1 or n == 2:
        return 1
    if n <= 20:
        if n < 3:
            return
        a = nacci[-1] + nacci[-2]
        nacci.append(a)
        fibo(n - 1)
        return nacci[-1]

num = int(input())
print(fibo(num))