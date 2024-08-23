import sys

def cut_paper(x,y,n):
    global paper, white, blue
    check = True # 같은 색상인지 확인했다는 뜻

    # 시작점
    start_paper = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            current_paper = paper[i][j]
            # 시작 점과 현재 점이 같은지 확인
            if start_paper != current_paper:
                check = False
                break

        if not check:
            break

    if check:
    # 색상 확인 0이면 White, 1이면 BLUE
        if start_paper == 0:
            white += 1

        elif start_paper == 1:
            blue += 1

    else:
        k = n // 2
        cut_paper(x, y, k)
        cut_paper(x, y + k, k)
        cut_paper(x + k, y, k)
        cut_paper(x + k, y + k, k)





n = int(input())
paper = []
for i in range(n):
    a = list(map(int, input().split()))
    paper.append(a)
white, blue  = 0, 0

cut_paper(0,0,n)
print(white)
print(blue)