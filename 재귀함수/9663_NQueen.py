# N - Queen
# https://www.acmicpc.net/problem/9663


def solve_n_queens(n):
    queens = [-1] * n
    count = 0 


    def is_valid(row, col): 
        for prev_row in range(row): 
            prev_col = queens[prev_row]

            if prev_col == col : 
                return False
            
            if abs(prev_row - row) == abs(prev_col - col): 
                return False
            
        return True

    def backTrack(row) : 
        nonlocal count 

        if row == n : 
            count += 1
            return 


        for col in range(n): 
            if is_valid(row, col): 
                queens[row] = col
                backTrack(row + 1)
                queens[row] = -1

    backTrack(0)
    return count 


n = int(input())
print(solve_n_queens(n))