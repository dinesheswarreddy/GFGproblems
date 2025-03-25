#Boolean Parenthesization
class Solution:
    def countWays(self, s: str) -> int:
        n = len(s)
        
        # DP tables to store the number of ways to evaluate to True and False
        dp_true = [[0] * n for _ in range(n)]
        dp_false = [[0] * n for _ in range(n)]
        
        # Base case: Single characters
        for i in range(n):
            if s[i] == 'T':
                dp_true[i][i] = 1
            elif s[i] == 'F':
                dp_false[i][i] = 1
        
        # Fill the DP tables for longer substrings
        for length in range(3, n + 1, 2):  # length of the substring (odd numbers)
            for i in range(n - length + 1):
                j = i + length - 1
                # Check all positions of the operator in the current substring
                for k in range(i + 1, j, 2):
                    op = s[k]
                    
                    # Calculate the number of ways for each combination of the operator
                    lt = dp_true[i][k - 1]
                    lf = dp_false[i][k - 1]
                    rt = dp_true[k + 1][j]
                    rf = dp_false[k + 1][j]
                    
                    if op == '&':
                        dp_true[i][j] += lt * rt
                        dp_false[i][j] += lt * rf + lf * rt + lf * rf
                    elif op == '|':
                        dp_true[i][j] += lt * rt + lt * rf + lf * rt
                        dp_false[i][j] += lf * rf
                    elif op == '^':
                        dp_true[i][j] += lt * rf + lf * rt
                        dp_false[i][j] += lt * rt + lf * rf
        
        return dp_true[0][n - 1]

# Example usage:
# 1. Predefined example
sol = Solution()
predefined_expr = "T|T&F^T"
print(f"Number of ways to evaluate '{predefined_expr}' to True: {sol.countWays(predefined_expr)}")  # Output: 4

# 2. Taking input from the user
user_expr = input("Enter a boolean expression (using 'T', 'F', '&', '|', '^'): ")
print(f"Number of ways to evaluate '{user_expr}' to True: {sol.countWays(user_expr)}")
