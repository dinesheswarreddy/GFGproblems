#N-Queen Problem
class Solution:
    def nQueen(self, n):
        def backtrack(c, sol, res):
            if c == n:
                res.append([s + 1 for s in sol])  # Adjusting to 1-based index
                return
            
            for r in range(n):
                if r in rows or (r - c) in main_diag or (r + c) in anti_diag:
                    continue
                
                sol[c] = r
                rows.add(r)
                main_diag.add(r - c)
                anti_diag.add(r + c)
                
                backtrack(c + 1, sol, res)
                
                rows.remove(r)
                main_diag.remove(r - c)
                anti_diag.remove(r + c)
        
        res = []
        sol = [-1] * n
        rows = set()
        main_diag = set()
        anti_diag = set()
        
        backtrack(0, sol, res)
        
        return res

# Example 1: Take input from the user
n = int(input("Enter the value of n: "))
solution = Solution()
print("Solutions for n =", n)
print(solution.nQueen(n))

# Example 2: Use an inbuilt test case
n = 4
solution = Solution()
print("Solutions for n =", n)
print(solution.nQueen(n))
