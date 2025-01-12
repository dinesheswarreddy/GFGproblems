#Trapping Rain Water
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        
        if n <= 1:
            return 0
        
        left, right = 0, n - 1
        max_l, max_r = arr[left], arr[right]
        water = 0
        
        while left <= right:
            if max_l <= max_r:
                if arr[left] < max_l:
                    water += max_l - arr[left]
                max_l = max(max_l, arr[left])
                left += 1
            else:
                if arr[right] < max_r:
                    water += max_r - arr[right]
                max_r = max(max_r, arr[right])
                right -= 1
        
        return water


# Example 1: Predefined input
arr1 = [3, 0, 1, 0, 4, 0, 2]
solution = Solution()
print(f"Water trapped (Predefined): {solution.maxWater(arr1)}")

# Example 2: Input from user
arr_input = list(map(int, input("Enter the array elements separated by space: ").split()))
print(f"Water trapped (User Input): {solution.maxWater(arr_input)}")
