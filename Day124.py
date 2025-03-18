#Partition Equal Subset Sum

class Solution:
    def equalPartition(self, arr):
        total_sum = sum(arr)
        
        # If the total sum is odd, it's not possible to partition into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(arr)
        
        # Create a DP array to store if a sum can be formed
        dp = [False] * (target + 1)
        dp[0] = True  # Sum of 0 is always possible with an empty subset
        
        for num in arr:
            # Update dp in reverse to avoid using the same number twice
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]

# Example 1: Hardcoded (Inbuilt) Input
arr_inbuilt = [1, 5, 11, 5]
solution = Solution()
print("Inbuilt Example: Can the array be partitioned into two subsets with equal sum?", solution.equalPartition(arr_inbuilt))

# Example 2: Taking Input from User
arr_user = list(map(int, input("Enter the array elements (space-separated): ").split()))
print("User Input Example: Can the array be partitioned into two subsets with equal sum?", solution.equalPartition(arr_user))
