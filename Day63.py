#Largest subarray of 0's and 1's
class Solution:
    def maxLen(self, arr):
        prefix_map = {0: -1}  # To handle case when the prefix sum is 0
        prefix_sum = 0
        max_len = 0
        for i, num in enumerate(arr):
            prefix_sum += 1 if num == 1 else -1
            if prefix_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum] = i
        return max_len


# Inbuilt Example Usage
arr1 = [1, 0, 1, 1, 1, 0, 0]
solution = Solution()
print(f"Max Length of Subarray with Equal 0s and 1s (Inbuilt Example): {solution.maxLen(arr1)}")

# User Input Example Usage
arr2 = list(map(int, input("Enter a binary array (space-separated values): ").split()))
print(f"Max Length of Subarray with Equal 0s and 1s (User Input Example): {solution.maxLen(arr2)}")
