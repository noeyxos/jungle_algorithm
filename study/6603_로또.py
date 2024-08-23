# 6603. 로또
# https://www.acmicpc.net/problem/6603

mport sys

input = sys.stdin.readline  # 표준 입력을 빠르게 받기 위해 sys.stdin.readline 사용

def print_visited(nums, visited, min_idx, level):
    if level == 6:  # 현재 선택된 숫자의 개수가 6개이면
        output = ""
        for i in range(len(nums)):  # 모든 숫자를 검사하여
            if visited[i]:  # 방문한 숫자들을
                output += str(nums[i]) + " "  # 출력 문자열에 추가
        print(output)  # 6개의 숫자로 이루어진 조합 출력
        return
    for nidx in range(min_idx, len(nums)):  # min_idx부터 시작하여 모든 숫자를 검사
        visited[nidx] = True  # 현재 숫자를 선택
        print_visited(nums, visited, nidx + 1, level + 1)  # 재귀 호출을 통해 다음 숫자를 선택
        visited[nidx] = False  # 현재 숫자를 선택 해제

while True:
    got = list(map(int, input().split(" ")))  # 입력 받은 문자열을 정수 리스트로 변환
    if len(got) == 1:  # 입력이 '0'으로 시작하면 (길이가 1인 경우)
        break  # 프로그램 종료
    N = got[0]  # 첫 번째 숫자는 총 숫자의 개수 (사용하지 않음)
    nums = got[1:]  # 나머지 숫자들을 nums 리스트에 저장
    visited = [False for _ in range(N)]  # 각 숫자의 방문 여부를 저장하는 리스트 초기화
    print_visited(nums, visited, 0, 0)  # 조합을 출력하는 함수 호출
    print()  # 각 테스트 케이스 사이에 빈 줄 출력
