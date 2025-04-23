#Unique Number II

class Solution:
    def singleNum(self, arr):
        xor_all = 0
        for num in arr:
            xor_all ^= num

        # Rightmost set bit
        rightmost_set_bit = xor_all & -xor_all

        num1 = 0
        num2 = 0
        for num in arr:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return sorted([num1, num2])


# Create object
sol = Solution()

# Built-in example usage
print("Built-in test cases:")
print(sol.singleNum([1, 2, 3, 2, 1, 4]))  # Output: [3, 4]
print(sol.singleNum([2, 1, 3, 2]))        # Output: [1, 3]
print(sol.singleNum([2, 1, 3, 3]))        # Output: [1, 2]

# User input
print("\nEnter the array elements separated by spaces:")
user_input = input()
user_arr = list(map(int, user_input.strip().split()))
result = sol.singleNum(user_arr)
print("The two unique numbers are:", result)
