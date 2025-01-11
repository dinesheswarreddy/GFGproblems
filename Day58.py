#Longest substring with distinct characters
class Solution:
    def longestUniqueSubstr(self, s: str) -> int:
        start = 0
        maxLength = 0
        charSet = set()

        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            
            charSet.add(s[end])
            maxLength = max(maxLength, end - start + 1)

        return maxLength


# Example 1: Predefined Input
solution = Solution()
predefined_input = "geeksforgeeks"
print("Predefined Input Example Output:")
print(solution.longestUniqueSubstr(predefined_input))  # Output: 7

# Example 2: User Input
print("\nUser Input Example:")
user_input = input("Enter a string: ")
print("Length of longest substring with unique characters:", solution.longestUniqueSubstr(user_input))
