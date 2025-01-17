#Product array puzzle
class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        res = [1] * n

        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= arr[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= arr[i]

        return res

# Example usage

# Inbuilt input
solution = Solution()
inbuilt_input = [10, 3, 5, 6, 2]
inbuilt_result = solution.productExceptSelf(inbuilt_input)
print("Inbuilt Input:", inbuilt_input)
print("Product Array (Inbuilt):", inbuilt_result)

# User input
user_input = list(map(int, input("Enter numbers separated by space: ").split()))
user_result = solution.productExceptSelf(user_input)
print("User Input:", user_input)
print("Product Array (User Input):", user_result)
