#Sum Pair closest to target
class Solution:
    def closest_pair(self, arr, target):
        arr.sort()
        left, right = 0, len(arr) - 1
        cs = float('inf')
        cp = []
        
        while left < right:
            curr_sum = arr[left] + arr[right]
            diff = abs(curr_sum - target)
            
            if diff < abs(cs - target):
                cs = curr_sum
                cp = [arr[left], arr[right]]
            elif diff == abs(cs - target):
                if abs(arr[left] - arr[right]) > abs(cp[0] - cp[1]):
                    cp = [arr[left], arr[right]]
            
            if curr_sum < target:
                left += 1
            else:
                right -= 1
                
        return cp

# Example usage
sol = Solution()

# Example 1
arr1 = [10, 30, 20, 5]
target1 = 25
print("Example 1:", sol.closest_pair(arr1, target1))  # Output: [5, 20]

# Example 2
arr2 = [5, 2, 7, 1, 4]
target2 = 10
print("Example 2:", sol.closest_pair(arr2, target2))  # Output: [2, 7]

# Example 3
arr3 = [10]
target3 = 10
print("Example 3:", sol.closest_pair(arr3, target3))  # Output: []

# Example 4 (User input case)
arr4 = list(map(int, input("Enter the array elements separated by spaces: ").split()))
target4 = int(input("Enter the target value: "))
print("Example 4:", sol.closest_pair(arr4, target4))
