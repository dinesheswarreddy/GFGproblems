#Set Matrix Zeroes
class Solution:
    def setMatrixZeroes(self, mat):
        r_zero = c_zero = False
        
        for j in range(len(mat[0])):
            if mat[0][j] == 0:
                r_zero = True
                break
        
        for i in range(len(mat)):
            if mat[i][0] == 0:
                c_zero = True
                break
        
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
        
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        if c_zero:
            for i in range(len(mat)):
                mat[i][0] = 0
        
        if r_zero:
            for j in range(len(mat[0])):
                mat[0][j] = 0
# Example usage of the Solution class

# Initialize the Solution class
sol = Solution()

# Define a matrix
mat = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

# Call the method to set matrix zeroes
sol.setMatrixZeroes(mat)

# Print the modified matrix
for row in mat:
    print(row)
