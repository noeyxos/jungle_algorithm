# # 부분수열의 합
# from itertools import combinations
#
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
#
# count = 0
#
# for i in range(1, n+1):
#     for comb in combinations(arr, i):
#         if sum(comb) == s:
#             count += 1
#
# print(count)


# # 부분 수열의 합
N,S = 5,0
# num = list(map(int, input().split()))
num = [-7 ,-3, -2, 5, 8]
cnt = 0
ans = []
def solve(start):
    global cnt
    if sum(ans) == S and len(ans) > 0:
        cnt += 1
    for i in range(start, N):
        ans.append(num[i])
        print('arr : ',ans,'\ncnt : ',cnt)
        print('='*20)
        print(f'{i+1}을 호출 할 것이다')
        solve(i+1)
        ans.pop()
solve(0)
print(cnt)