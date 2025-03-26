#Word Break

class Solution:
    def wordBreak(self, s, dictionary):
        word_set = set(dictionary)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        max_len = max(len(word) for word in word_set)
        
        for i in range(1, len(s) + 1):
            for j in range(i - max_len, i):
                if j >= 0 and dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

# Example 1: Inbuilt Test Case
solution = Solution()
s = "ilike"
dictionary = ["i", "like", "gfg"]
print(solution.wordBreak(s, dictionary))  # Output: True

# Example 2: Take input from user
s = input("Enter the string: ")
dictionary_input = input("Enter words for dictionary (separate by space): ").split()
solution = Solution()
print(solution.wordBreak(s, dictionary_input))
