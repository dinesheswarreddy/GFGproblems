#Count Subarrays with given XOR
class Solution:
    def countSubarraysWithXOR(self, arr, k):
        prefix_XOR = 0
        prefix_count = {}
        result = 0

        prefix_count[0] = 1
        
        for num in arr:
            prefix_XOR ^= num
            
            if prefix_XOR ^ k in prefix_count:
                result += prefix_count[prefix_XOR ^ k]
            
            if prefix_XOR in prefix_count:
                prefix_count[prefix_XOR] += 1
            else:
                prefix_count[prefix_XOR] = 1
        
        return result

# Example usage:
solution = Solution()

# Example 1
arr1 = [4, 2, 2, 6, 4]
k1 = 6
print(f"Example 1 result: {solution.countSubarraysWithXOR(arr1, k1)}")  # Output: 4

# Example 2
arr2 = [5, 6, 7, 8, 9]
k2 = 5
print(f"Example 2 result: {solution.countSubarraysWithXOR(arr2, k2)}")  # Output: 2

# Example 3
arr3 = [1, 1, 1, 1]
k3 = 0
print(f"Example 3 result: {solution.countSubarraysWithXOR(arr3, k3)}")  # Output: 4
