#Palindrome SubStrings

class Solution:
    def countPS(self, s: str) -> int:
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 >= 2:  # Only count substrings of length >= 2
                    count += 1
                left -= 1
                right += 1
            return count
        
        total_count = 0
        for i in range(len(s)):
            # Odd length palindromes
            total_count += expand_around_center(i, i)
            # Even length palindromes
            total_count += expand_around_center(i, i + 1)
        
        return total_count

# Create an instance of the Solution class
sol = Solution()

# Example 1: Inbuilt test case
print("Test case 1 (inbuilt):")
print(sol.countPS("abaab"))  # Expected output: 3

# Example 2: Taking input from the user
print("\nTest case 2 (user input):")
user_input = input("Enter a string: ")
print(sol.countPS(user_input))
