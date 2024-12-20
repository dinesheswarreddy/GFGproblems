#Spirally traversing a matrix

class Solution:
    def spirallyTraverse(self, mat):
        if not mat:
            return []
        
        n = len(mat)       # Number of rows
        m = len(mat[0])    # Number of columns
        result = []
        
        top, bottom, left, right = 0, n - 1, 0, m - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            
            # Traverse downwards along the right column
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            # Traverse from right to left along the bottom row
            if top <= bottom:  # Check if there is a bottom row remaining
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
            
            # Traverse upwards along the left column
            if left <= right:  # Check if there is a left column remaining
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        
        return result
# Example
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Create a Solution object
sol = Solution()

# Call the spirallyTraverse method
result = sol.spirallyTraverse(mat)

# Output the result
print(result)
