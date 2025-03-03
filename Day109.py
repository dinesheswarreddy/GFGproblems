#Longest Bounded-Difference Subarray
from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        n = len(arr)
        
        # Deques to store indices of the max and min elements in the current window
        max_deque = deque()
        min_deque = deque()
        
        left = 0
        longest_len = 0
        start_index = 0
        
        for right in range(n):
            # Maintain the max deque
            while max_deque and arr[max_deque[-1]] <= arr[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain the min deque
            while min_deque and arr[min_deque[-1]] >= arr[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Check if the current window is valid
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                left += 1  # Shrink the window from the left
                # Remove elements that are out of the window range
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the longest subarray if the current window is valid
            if right - left + 1 > longest_len:
                longest_len = right - left + 1
                start_index = left
        
        # Return the longest subarray
        return arr[start_index:start_index + longest_len]

# Inbuilt example
arr_inbuilt = [15, 10, 1, 2, 4, 7, 2]
x_inbuilt = 5
sol = Solution()
result_inbuilt = sol.longestSubarray(arr_inbuilt, x_inbuilt)
print(f"Longest subarray (inbuilt): {result_inbuilt}")

# User input example
arr_input = list(map(int, input("Enter the array of integers (space-separated): ").split()))
x_input = int(input("Enter the value of x: "))
result_input = sol.longestSubarray(arr_input, x_input)
print(f"Longest subarray (user input): {result_input}")
