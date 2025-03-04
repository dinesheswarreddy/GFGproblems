#Longest Increasing Subsequence

class Solution:
    def lis(self, arr):
        n = len(arr)
        
        # dp[i] will hold the length of LIS ending at arr[i]
        dp = [1] * n
        
        # Build the dp array
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The length of the Longest Increasing Subsequence will be the max value in dp
        return max(dp)

# Example 1: Taking input from the user
arr_input = list(map(int, input("Enter the array elements separated by space: ").split()))
sol = Solution()
print(f"Length of Longest Increasing Subsequence: {sol.lis(arr_input)}")

# Example 2: Inbuilt test case
arr_inbuilt = [5, 8, 3, 7, 9, 1]
print(f"Length of Longest Increasing Subsequence for inbuilt array: {sol.lis(arr_inbuilt)}")
