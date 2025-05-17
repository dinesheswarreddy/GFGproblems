#Sort the given array after applying the given equation
class Solution:
    def sortArray(self, arr, A, B, C):
        def quad(x):
            return A * x * x + B * x + C

        n = len(arr)
        result = [0] * n
        left, right = 0, n - 1
        index = n - 1 if A >= 0 else 0  # Fill from end if A > 0, else from start

        while left <= right:
            left_val = quad(arr[left])
            right_val = quad(arr[right])

            if A >= 0:
                if left_val > right_val:
                    result[index] = left_val
                    left += 1
                else:
                    result[index] = right_val
                    right -= 1
                index -= 1
            else:
                if left_val < right_val:
                    result[index] = left_val
                    left += 1
                else:
                    result[index] = right_val
                    right -= 1
                index += 1

        return result


# === Built-in Example Usage ===
print("Built-in Examples:")
s = Solution()
print("Example 1 Output:", s.sortArray([-4, -2, 0, 2, 4], 1, 3, 5))  # [3, 5, 9, 15, 33]
print("Example 2 Output:", s.sortArray([-3, -1, 2, 4], -1, 0, 0))    # [-16, -9, -4, -1]

# === User Input ===
print("\nCustom Input:")
try:
    arr_input = list(map(int, input("Enter sorted array elements (space-separated): ").split()))
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    C = int(input("Enter C: "))
    result = s.sortArray(arr_input, A, B, C)
    print("Transformed and Sorted Array:", result)
except Exception as e:
    print("Invalid input. Error:", e)
