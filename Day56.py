#Indexes of Subarray Sum
class Solution:
    def subarraySum(self, arr, target):
        start = 0
        current_sum = 0
        
        for end in range(len(arr)):
            current_sum += arr[end]
            
            while current_sum > target and start <= end:
                current_sum -= arr[start]
                start += 1
            
            if current_sum == target:
                return [start + 1, end + 1]

        return [-1]

# Example 1: Predefined usage
solution = Solution()
arr1 = [1, 2, 3, 7, 5]
target1 = 12
print(f"Example 1: {solution.subarraySum(arr1, target1)}")  # Output: [2, 4]

# Example 2: Input taken from user
arr2 = list(map(int, input("Enter the array elements separated by spaces: ").split()))
target2 = int(input("Enter the target value: "))
print(f"Example 2: {solution.subarraySum(arr2, target2)}")
