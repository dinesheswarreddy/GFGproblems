#Stickler Thief II

class Solution:
    def maxValue(self, arr):
        n = len(arr)
        
        # Edge case: if there are only two houses, rob the maximum of the two
        if n == 2:
            return max(arr[0], arr[1])
        
        # Helper function to compute the maximum stolen value in a linear arrangement
        def houseRobber(arr):
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]
            
            # dp array to store maximum value at each step
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            
            return dp[n-1]
        
        # Case 1: Rob houses from index 0 to n-2 (excluding the last house)
        case1 = houseRobber(arr[:-1])
        
        # Case 2: Rob houses from index 1 to n-1 (excluding the first house)
        case2 = houseRobber(arr[1:])
        
        # Return the maximum of both cases
        return max(case1, case2)


# Inbuilt array example
solution = Solution()

inbuilt_arr = [2, 3, 2]
print("Inbuilt Example - Max stolen value:", solution.maxValue(inbuilt_arr))

# User-defined array example
user_input = input("Enter house values separated by space: ")
user_arr = list(map(int, user_input.split()))  # Convert the input to a list of integers

print("User-defined Example - Max stolen value:", solution.maxValue(user_arr))
