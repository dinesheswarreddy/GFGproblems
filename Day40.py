#Search in a sorted Matrix
class Solution:   
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
        # code here 
        if not mat:
            return False
        n = len(mat)
        m = len(mat[0])
        row = 0
        col = m - 1
        while row < n and col >= 0:
            if mat[row][col] == x:
                return True
            elif mat[row][col] > x:
                col -= 1
            else:
                row += 1
        return False
# Create an object of the Solution class
solution = Solution()

# Test case 1
mat1 = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
x1 = 14
print(solution.searchMatrix(mat1, x1))  # Output: True

# Test case 2
mat2 = [[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]]
x2 = 42
print(solution.searchMatrix(mat2, x2))  # Output: False

# Test case 3
mat3 = [[87, 96, 99], [101, 103, 111]]
x3 = 101
print(solution.searchMatrix(mat3, x3))  # Output: True


