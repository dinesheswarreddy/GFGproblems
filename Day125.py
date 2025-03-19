#Stock Buy and Sell – Max K Transactions Allowed

class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        
        if n == 0 or k == 0:
            return 0
        
        # If k is greater than or equal to n//2, we can make unlimited transactions
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
        
        # DP array where dp[i][j] represents the max profit with at most i transactions by day j
        dp = [[0] * n for _ in range(k+1)]
        
        # Iterate over all transaction counts from 1 to k
        for i in range(1, k+1):
            # Initialize max_diff to a very low number
            max_diff = -prices[0]
            
            # Iterate over all days from 1 to n-1
            for j in range(1, n):
                # The maximum of either not doing a transaction today or selling today
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                
                # Update max_diff: max of current max_diff or dp[i-1][j] - prices[j]
                max_diff = max(max_diff, dp[i-1][j] - prices[j])
        
        return dp[k][n-1]

# Example 1: Inbuilt Example
prices_inbuilt = [10, 22, 5, 80]
k_inbuilt = 2
solution = Solution()
print(f"Max profit for inbuilt example: {solution.maxProfit(prices_inbuilt, k_inbuilt)}")

# Example 2: Taking input from the user
prices_user_input = list(map(int, input("Enter stock prices separated by spaces: ").split()))
k_user_input = int(input("Enter the maximum number of transactions allowed: "))
print(f"Max profit for user input: {solution.maxProfit(prices_user_input, k_user_input)}")
