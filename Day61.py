#Equilibrium Point
class Solution:
    # Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)  # Sum of all elements in the array
        left_sum = 0  # This will store the sum of elements on the left of current index
        
        for i in range(len(arr)):
            total_sum -= arr[i]  # Subtract the current element from total sum to get right sum
            
            if left_sum == total_sum:  # If left sum equals right sum, we found the equilibrium point
                return i
            
            left_sum += arr[i]  # Add current element to left sum
        
        return -1  # Return -1 if no equilibrium point is found


# Example 1: Predefined input
arr1 = [1, 2, 0, 3]
solution = Solution()
result1 = solution.findEquilibrium(arr1)
print(f"Equilibrium index for arr1: {result1}")  # Output should be 2

# Example 2: Input taken from user
arr2 = list(map(int, input("Enter the array elements (space-separated): ").split()))
solution = Solution()
result2 = solution.findEquilibrium(arr2)
print(f"Equilibrium index for arr2: {result2}")
