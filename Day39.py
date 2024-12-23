#Search in a row-wise sorted matrix
class Solution:
    def searchMatrix(self, mat, x):
        for row in mat:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == x:
                    return True
                elif row[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

# Example usage:
solution = Solution()

matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]

# Search for the value 5
result = solution.searchMatrix(matrix, 5)
print("Found 5:", result)  # Output: True

# Search for the value 20
result = solution.searchMatrix(matrix, 20)
print("Found 20:", result)  # Output: False
