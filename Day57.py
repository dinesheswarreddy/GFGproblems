#Count distinct elements in every window
from collections import defaultdict

class Solution:
    def countDistinct(self, arr, k):
        freq_map = defaultdict(int)
        result = []

        for i in range(k):
            freq_map[arr[i]] += 1
        
        result.append(len(freq_map))
        
        for i in range(k, len(arr)):
            freq_map[arr[i - k]] -= 1
            if freq_map[arr[i - k]] == 0:
                del freq_map[arr[i - k]]
            
            freq_map[arr[i]] += 1
            result.append(len(freq_map))
        
        return result

# Predefined Example
solution = Solution()
arr1 = [1, 2, 1, 3, 4, 2, 3]
k1 = 4
print("Predefined Input Example Output:")
print(solution.countDistinct(arr1, k1))  # Output: [3, 4, 4, 3]

# Input from User
print("\nUser Input Example:")
arr2 = list(map(int, input("Enter the array elements (space separated): ").split()))
k2 = int(input("Enter the window size (k): "))
print(solution.countDistinct(arr2, k2))
