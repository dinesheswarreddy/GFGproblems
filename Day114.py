#Longest Palindrome in a String
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        result = ""
        
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        
        return result


# Inbuilt example
s1 = "forgeeksskeegfor"
solution = Solution()
print("Longest Palindrome (Inbuilt):", solution.longestPalindrome(s1))

# User input example
s2 = input("Enter a string: ")
print("Longest Palindrome (User Input):", solution.longestPalindrome(s2))
