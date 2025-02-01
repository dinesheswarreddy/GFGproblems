#Word Search
class Solution:
    def isWordExist(self, mat, word):
        def dfs(mat, word, i, j, index, visited):
            if index == len(word):
                return True
            if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or visited[i][j] or mat[i][j] != word[index]:
                return False
            visited[i][j] = True
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if dfs(mat, word, new_i, new_j, index + 1, visited):
                    return True
            visited[i][j] = False
            return False

        if not mat or not word:
            return False
        
        visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == word[0]:
                    if dfs(mat, word, i, j, 0, visited):
                        return True
        
        return False

# Example 1: Inbuilt example
solution = Solution()
mat1 = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']]
word1 = "GEEK"
print("Inbuilt example result:", solution.isWordExist(mat1, word1))  # Output: True

# Example 2: Input taken from the user
mat2 = []
n = int(input("Enter the number of rows in the matrix: "))
m = int(input("Enter the number of columns in the matrix: "))
for i in range(n):
    row = input(f"Enter row {i + 1} (space-separated characters): ").split()
    mat2.append(row)

word2 = input("Enter the word to search: ")
print("User input example result:", solution.isWordExist(mat2, word2))
