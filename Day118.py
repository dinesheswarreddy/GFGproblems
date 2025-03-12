#Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        
        # Handle base cases
        if n == 2:
            return min(cost[0], cost[1])
        
        # Use two variables to keep track of the last two minimum costs
        prev1 = cost[0]  # cost to reach the first step
        prev2 = cost[1]  # cost to reach the second step
        
        for i in range(2, n):
            current = min(prev1, prev2) + cost[i]
            prev1, prev2 = prev2, current
        
        # The answer is the minimum cost to reach the top
        return min(prev1, prev2)

# Example 1: Input taken from the user
print("Example 1: Input taken from the user")
cost_input = input("Enter the costs of the stairs (comma-separated): ")
cost = list(map(int, cost_input.split(',')))
solution = Solution()
print(f"Minimum cost to reach the top: {solution.minCostClimbingStairs(cost)}")

# Example 2: Inbuilt test case
print("\nExample 2: Inbuilt test case")
cost_inbuilt = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(f"Minimum cost to reach the top: {solution.minCostClimbingStairs(cost_inbuilt)}")
