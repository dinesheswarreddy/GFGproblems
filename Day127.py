#Stickler Thief

class Solution:
    def findMaxSum(self, arr):
        # Handle base cases
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 2:
            return max(arr[0], arr[1])

        # Initialize the two variables to track the previous two results
        prev2 = arr[0]  # dp[i-2]
        prev1 = max(arr[0], arr[1])  # dp[i-1]
        
        # Iterate through the array starting from the 3rd element
        for i in range(2, len(arr)):
            current = max(prev1, arr[i] + prev2)  # dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            prev2 = prev1  # Move prev1 to prev2
            prev1 = current  # Update prev1 to the current value
        
        # The result is stored in prev1
        return prev1

# Inbuilt example
inbuilt_example = [6, 5, 5, 7, 4]
solution = Solution()
print("Inbuilt Example Result:", solution.findMaxSum(inbuilt_example))

# Taking an array as input from the user
user_input = input("Enter the amounts in the houses (comma-separated): ")
user_arr = list(map(int, user_input.split(',')))
print("User Input Example Result:", solution.findMaxSum(user_arr))
