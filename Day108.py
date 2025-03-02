#K Sized Subarray Maximum
from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        # Initialize the deque and the result list
        dq = deque()
        result = []
        
        for i in range(len(arr)):
            # Remove elements from the front of the deque if they are out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove elements from the back of the deque that are smaller than the current element
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            # Add the current element's index to the deque
            dq.append(i)
            
            # The first k-1 windows will not have a valid result, so we start adding results
            if i >= k - 1:
                result.append(arr[dq[0]])  # The maximum element for the current window is at the front of the deque
        
        return result


# Example 1: Inbuilt test case
solution = Solution()
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
print(f"Inbuilt test case: {arr}, k={k}")
print(f"Output: {solution.maxOfSubarrays(arr, k)}")

# Example 2: User input
arr_input = input("Enter the array of integers (space-separated): ").split()
arr = list(map(int, arr_input))
k_input = int(input("Enter the value of k: "))

print(f"User input array: {arr}, k={k_input}")
print(f"Output: {solution.maxOfSubarrays(arr, k_input)}")
