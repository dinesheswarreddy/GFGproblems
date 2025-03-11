#Ways to Reach the n'th Stair

class Solution:
    def countWays(self, n):
        # Base cases:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # dp array to store the number of ways to reach each stair
        dp = [0] * (n + 1)
        
        # Base cases initialization
        dp[1] = 1
        dp[2] = 2
        
        # Fill dp array for all stairs from 3 to n
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # The result will be the number of ways to reach the nth stair
        return dp[n]

# Example 1: Inbuilt Example
solution = Solution()
inbuilt_input = 4
print(f"Example 1 (Inbuilt Input): Number of ways to reach the {inbuilt_input}th stair is {solution.countWays(inbuilt_input)}")

# Example 2: User Input
user_input = int(input("Enter the number of stairs: "))
print(f"Example 2 (User Input): Number of ways to reach the {user_input}th stair is {solution.countWays(user_input)}")
