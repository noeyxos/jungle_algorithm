t = int(input())

for _ in range(t):
    r, s = input().split()
    text =''
    for i in s:
        text += int(r)*i
    print(text)