#Majority Element

class Solution:
    def majorityElement(self, arr):
        # Phase 1: Find the candidate for majority element
        candidate = None
        count = 0
        
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Phase 2: Verify the candidate
        count = 0
        for num in arr:
            if num == candidate:
                count += 1
        
        # Check if the candidate appears more than n//2 times
        if count > len(arr) // 2:
            return candidate
        else:
            return -1

# Example with inbuilt data
solution = Solution()

# Test case 1: Hardcoded example
arr1 = [1, 1, 2, 1, 3, 5, 1]
print(f"Example 1 - Majority Element: {solution.majorityElement(arr1)}")

# Test case 2: Another hardcoded example
arr2 = [7]
print(f"Example 2 - Majority Element: {solution.majorityElement(arr2)}")

# Test case 3: Another hardcoded example
arr3 = [2, 13]
print(f"Example 3 - Majority Element: {solution.majorityElement(arr3)}")

# Now, take user input
print("\nEnter an array of integers (space-separated):")
user_input = input()  # Take input as a string
arr_user = list(map(int, user_input.split()))  # Convert the input string to a list of integers

# Find and display the majority element for the user input
print(f"User Input - Majority Element: {solution.majorityElement(arr_user)}")
