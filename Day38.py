#Search in a Row-Column sorted matrix
class Solution:
    def matSearch(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        row, col = 0, m - 1
        
        while row < n and col >= 0:
            if mat[row][col] == x:
                return True
            elif mat[row][col] < x:
                row += 1
            else:
                col -= 1
        
        return False

# Example usage:
sol = Solution()
mat = [[3, 30, 38], [20, 52, 54], [35, 60, 69]]
x = 62
print(sol.matSearch(mat, x))  # Output: False

mat = [[18, 21, 27], [38, 55, 67]]
x = 55
print(sol.matSearch(mat, x))  # Output: True

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 3
print(sol.matSearch(mat, x))  # Output: True
