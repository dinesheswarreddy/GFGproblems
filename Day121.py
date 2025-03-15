#Coin Change (Minimum Coins)

class Solution:
    def minCoins(self, coins, sum):
        dp = [float('inf')] * (sum + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[sum] if dp[sum] != float('inf') else -1

# Example 1: Inbuilt test case
coins = [25, 10, 5]
sum = 30
solution = Solution()
print(solution.minCoins(coins, sum))  # Output: 2

# Example 2: User input test case
coins = list(map(int, input("Enter the coin denominations: ").split()))
sum = int(input("Enter the target sum: "))
print(solution.minCoins(coins, sum))
