#Permutations of a String
class Solution:
    def findPermutation(self, s):
        # Code here
        def backtrack(path, counter):
            if len(path) == len(s):
                result.append(''.join(path))
                return
            for char in counter:
                if counter[char] > 0:
                    path.append(char)
                    counter[char] -= 1
                    backtrack(path, counter)
                    path.pop()
                    counter[char] += 1

        result = []
        counter = {char: s.count(char) for char in set(s)}
        backtrack([], counter)
        return result


# Example 1: Inbuilt test case
s_inbuilt = "ABC"
solution = Solution()
print("Inbuilt test case output:")
print(solution.findPermutation(s_inbuilt))

# Example 2: Taking input from user
s_user = input("Enter a string to find its unique permutations: ")
print("User input test case output:")
print(solution.findPermutation(s_user))
