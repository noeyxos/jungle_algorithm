# 더하기 사이클


n = int(input())
ans = n
count = 0

while True:
    a = ans // 10
    b = ans % 10
    c = (a+b) % 10
    ans = (b*10) + c
    count += 1
    if(ans == n):
        break
print(count)