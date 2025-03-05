#Longest String Chain

class Solution:
    def longestStringChain(self, words):
        words.sort(key=len)
        
        dp = {}
        max_chain = 1
        
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            max_chain = max(max_chain, dp[word])
        
        return max_chain

# Inbuilt example
solution = Solution()
words_inbuilt = ["ba", "b", "a", "bca", "bda", "bdca"]
print(f"Inbuilt Example: {solution.longestStringChain(words_inbuilt)}")

# User input example
words_user = input("Enter words separated by space: ").split()
print(f"User Input Example: {solution.longestStringChain(words_user)}")
