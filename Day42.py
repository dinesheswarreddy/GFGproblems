#Two Sum - Pair with Given Sum
# User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        # code here
        s = set()
        for n in arr:
            if target - n in s:
                return True
            s.add(n)
        return False

# Example usage
sol = Solution()

# Example 1
arr1 = [1, 4, 45, 6, 10, 8]
target1 = 16
print(sol.twoSum(arr1, target1))  # Output: True (because 6 + 10 = 16)

# Example 2
arr2 = [1, 2, 4, 3, 6]
target2 = 11
print(sol.twoSum(arr2, target2))  # Output: False (no pair sums up to 11)
