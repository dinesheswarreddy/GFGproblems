#Count Pairs whose sum is less than target
class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        # Initialize variables
        count, left, right = 0, 0, len(arr) - 1
        
        # Sort the array
        arr.sort()
        
        # Two-pointer approach
        while left < right:
            if arr[left] + arr[right] < target:
                # If sum of arr[left] and arr[right] is less than target, count all pairs between left and right
                count += (right - left)
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left
        
        return count

# Example usage
if __name__ == "__main__":
    # Take user input
    arr = list(map(int, input("Enter the array (space separated): ").split()))
    target = int(input("Enter the target: "))
    
    # Create an instance of Solution class
    solution = Solution()
    
    # Get the result
    result = solution.countPairs(arr, target)
    
    # Print the result
    print(f"Number of pairs with sum less than {target}: {result}")
# Example 1
arr1 = [7, 2, 5, 3]
target1 = 8
result1 = sol.countPairs(arr1, target1)
print(f"Example 1 Result: {result1}")  # Expected Output: 2

# Example 2
arr2 = [5, 2, 3, 2, 4, 1]
target2 = 5
result2 = sol.countPairs(arr2, target2)
print(f"Example 2 Result: {result2}")  # Expected Output: 4

# Example 3
arr3 = [2, 1, 8, 3, 4, 7, 6, 5]
target3 = 7
result3 = sol.countPairs(arr3, target3)
print(f"Example 3 Result: {result3}")  # Expected Output: 6
