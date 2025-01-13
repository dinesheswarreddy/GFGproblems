#Container With Most Water
class Solution:
    def maxWater(self, arr):
        left = 0
        right = len(arr) - 1
        max_area = 0
        
        while left < right:
            height = min(arr[left], arr[right])
            width = right - left
            area = height * width
            max_area = max(max_area, area)
            
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example 1: Predefined input
arr1 = [1, 5, 4, 3]
solution = Solution()
print("Maximum Water (Predefined):", solution.maxWater(arr1))

# Example 2: Input taken from the user
arr2 = list(map(int, input("Enter the array of heights (space separated): ").split()))
print("Maximum Water (User Input):", solution.maxWater(arr2))
