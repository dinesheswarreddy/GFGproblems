#Rotate by 90 degree

class Solution:
    
    def rotateby90(self, mat): 
        n = len(mat)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        # Step 2: Reverse the rows
        for j in range(n):
            for i in range(n // 2):
                mat[i][j], mat[n-i-1][j] = mat[n-i-1][j], mat[i][j]

# Example usage
mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol = Solution()
sol.rotateby90(mat1)
for row in mat1:
    print(row)

mat2 = [[1, 2], [3, 4]]
sol.rotateby90(mat2)
for row in mat2:
    print(row)
