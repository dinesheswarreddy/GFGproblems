#Stock Buy and Sell – Max 2 Transactions Allowed

class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        first_buy = -prices[0]
        first_sell = 0
        second_buy = -prices[0]
        second_sell = 0
        
        for price in prices:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)
        
        return second_sell

# Example 1: Inbuilt prices array
prices_inbuilt = [10, 22, 5, 75, 65, 80]
solution = Solution()
print(solution.maxProfit(prices_inbuilt))  # Output: 87

# Example 2: User input
prices_user_input = list(map(int, input("Enter stock prices separated by spaces: ").split()))
solution = Solution()
print(solution.maxProfit(prices_user_input))
