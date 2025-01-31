#Solve the Sudoku
class Solution:
    
    def solveSudoku(self, mat):
        
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]
        
        # Fill in the sets with the initial numbers from the board
        for r in range(9):
            for c in range(9):
                if mat[r][c] != 0:
                    row_sets[r].add(mat[r][c])
                    col_sets[c].add(mat[r][c])
                    box_sets[(r // 3) * 3 + (c // 3)].add(mat[r][c])
        
        def is_valid(r, c, num):
            box_index = (r // 3) * 3 + (c // 3)
            if num in row_sets[r] or num in col_sets[c] or num in box_sets[box_index]:
                return False
            return True
        
        def solve():
            for r in range(9):
                for c in range(9):
                    if mat[r][c] == 0:
                        for num in range(1, 10):
                            if is_valid(r, c, num):
                                mat[r][c] = num
                                row_sets[r].add(num)
                                col_sets[c].add(num)
                                box_sets[(r // 3) * 3 + (c // 3)].add(num)
                                
                                if solve():
                                    return True
                                
                                mat[r][c] = 0
                                row_sets[r].remove(num)
                                col_sets[c].remove(num)
                                box_sets[(r // 3) * 3 + (c // 3)].remove(num)
                        return False
            return True
        
        solve()
        return mat

# Example 1: Inbuilt Sudoku board
print("Inbuilt Sudoku Solution:")
solution = Solution()
mat_inbuilt = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solved_inbuilt = solution.solveSudoku(mat_inbuilt)
for row in solved_inbuilt:
    print(row)

# Example 2: User Input Sudoku
print("\nUser Input Sudoku Solution:")
solution = Solution()
mat_user = []

print("Enter the Sudoku puzzle row by row (use 0 for empty cells):")
for i in range(9):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    mat_user.append(row)

solved_user = solution.solveSudoku(mat_user)
for row in solved_user:
    print(row)
