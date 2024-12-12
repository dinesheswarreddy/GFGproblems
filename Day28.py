#Number of occurrence

class Solution:
    def countFreq(self, arr, target):
        # Initialize a counter to 0
        count = 0
        
        # Iterate through each element in the list
        for num in arr:
            # If the element matches the target, increment the counter
            if num == target:
                count += 1
        
        # Return the final count
        return count
# Create an object of Solution
solution = Solution()

# Define an array and the target number to count
arr = [1, 2, 3, 2, 2, 4, 5, 2]
target = 2

# Call the countFreq method
result = solution.countFreq(arr, target)

# Print the result
print(result)  # Output: 4
