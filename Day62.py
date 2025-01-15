#Longest Subarray with Sum K
class Solution:
    def longestSubarrayWithSumK(self, arr, k):
        prefix_sum = 0
        prefix_map = {0: -1}
        max_length = 0
        
        for i, num in enumerate(arr):
            prefix_sum += num
            
            if prefix_sum - k in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum - k])
            
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        
        return max_length

# Example usage with built-in input
solution = Solution()
print(solution.longestSubarrayWithSumK([10, 5, 2, 7, 1, -10], 15))  # Output: 6

# Example usage with user input
arr_input = list(map(int, input("Enter the array elements separated by space: ").split()))
k_input = int(input("Enter the value of k: "))
print(solution.longestSubarrayWithSumK(arr_input, k_input))
