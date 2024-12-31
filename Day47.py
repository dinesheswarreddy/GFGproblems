#Longest Consecutive Subsequence
# Define the Solution class
class Solution:
    def longestConsecutive(self, arr):
        nums = set(arr)  # Convert the list to a set for O(1) lookup
        length = 0  # Variable to store the length of the longest consecutive subsequence
        for i in nums:
            # Start a new sequence if i-1 is not in the set
            if i - 1 not in nums:
                cur = i  # Start with the current number
                count = 1  # Count this number
                while cur + 1 in nums:  # Keep going as long as the next number is in the set
                    cur += 1
                    count += 1
                length = max(length, count)  # Update the maximum length found
        return length

# Example 1
arr1 = [2, 6, 1, 9, 4, 5, 3]
sol = Solution()
print(sol.longestConsecutive(arr1))  # Output: 6

# Example 2
arr2 = [1, 9, 3, 10, 4, 20, 2]
print(sol.longestConsecutive(arr2))  # Output: 4

# Example 3
arr3 = [15, 13, 12, 14, 11, 10, 9]
print(sol.longestConsecutive(arr3))  # Output: 7
