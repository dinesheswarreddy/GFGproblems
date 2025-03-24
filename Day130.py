#Matrix Chain Multiplication

class Solution:
    def matrixMultiplication(self, arr):
        # Length of the matrix chain (number of matrices + 1)
        n = len(arr)
        
        # dp[i][j] will store the minimum number of multiplications needed to multiply matrices from i to j
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # l is the chain length
        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                # Try all possible positions for splitting the chain between i and j
                for k in range(i, j):
                    q = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], q)
        
        return dp[1][n-1]


# Example 1: Inbuilt example
arr_inbuilt = [2, 1, 3, 4]
solution = Solution()
print("Inbuilt Example Output:", solution.matrixMultiplication(arr_inbuilt))

# Example 2: User input example
arr_input = list(map(int, input("Enter the matrix dimensions (space-separated): ").split()))
solution = Solution()
print("User Input Example Output:", solution.matrixMultiplication(arr_input))
