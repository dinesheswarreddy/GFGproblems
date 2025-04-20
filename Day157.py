#Find Only Repetitive Element from 1 to n-1
class Solution:
    def findDuplicate(self, arr):
        n = len(arr)
        expected_sum = (n - 1) * n // 2  # Sum of 1 to n-1
        actual_sum = sum(arr)
        return actual_sum - expected_sum

# Create an instance of Solution
s = Solution()

# 🔹 Example usage with hardcoded array
print("🔸 Example (Inbuilt):")
example_arr = [1, 3, 2, 3, 4]
print(f"Input array: {example_arr}")
print(f"Duplicate element: {s.findDuplicate(example_arr)}\n")

# 🔹 User input section
print("🔹 Custom Input:")
user_input = input("Enter the array elements separated by space: ")
arr = list(map(int, user_input.strip().split()))
print(f"Duplicate element: {s.findDuplicate(arr)}")
