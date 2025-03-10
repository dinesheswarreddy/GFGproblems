#Edit Distance

class Solution:
    def editDistance(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        return dp[m][n]

# Inbuilt Example
solution = Solution()
s1 = "abcd"
s2 = "bcfe"
print(f"Edit Distance (Inbuilt): {solution.editDistance(s1, s2)}")

# User Input Example
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(f"Edit Distance (User Input): {solution.editDistance(s1, s2)}")
