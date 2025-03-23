#Total Decoding Messages

class Solution:
    def countWays(self, digits):
        # Edge case: if the string starts with '0', no valid decoding is possible
        if digits[0] == '0':
            return 0
        
        n = len(digits)
        
        # dp[i] will store the number of ways to decode the first i characters
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # There's one way to decode an empty string
        dp[1] = 1  # There's one way to decode a single character (as long as it's not '0')
        
        for i in range(2, n + 1):
            # Check if the current single digit can form a valid character
            if '1' <= digits[i-1] <= '9':  # Valid single character mapping
                dp[i] += dp[i-1]
            
            # Check if the current two digits can form a valid character
            if '10' <= digits[i-2:i] <= '26':  # Valid two character mapping
                dp[i] += dp[i-2]
        
        return dp[n]

# Example 1: Take input from the user
user_input = input("Enter a string of digits: ")
solution = Solution()
print(f"Number of ways to decode the user input: {solution.countWays(user_input)}")

# Example 2: Predefined inbuilt input
inbuilt_input = "123"
print(f"Number of ways to decode the inbuilt input: {solution.countWays(inbuilt_input)}")
