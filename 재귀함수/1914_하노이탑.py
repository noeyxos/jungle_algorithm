# 1914번 하노이 탑
# https://www.acmicpc.net/problem/1914

def hanoi_top(rings, start, end): 
		if rings == 1:
			print(start, end)
			return 
		
		elif rings <= 20 : 
			hanoi_top(rings-1, start, 6-start-end)
			print(start, end)
			hanoi_top(rings-1, 6-start-end, end)
		
		
rings = int(input()) # 원판의 갯수 
print(2 ** rings-1) # 최소 이동 횟수
hanoi_top(rings, 1, 3)