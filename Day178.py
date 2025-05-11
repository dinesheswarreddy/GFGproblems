#K-th Largest Sum Contiguous Subarray
from typing import List
import heapq

class Solution:
    def kthLargest(self, arr: List[int], k: int) -> int:
        min_heap = []
        n = len(arr)
        
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                heapq.heappush(min_heap, curr_sum)
                if len(min_heap) > k:
                    heapq.heappop(min_heap)
                    
        return min_heap[0]

# Built-in Example Usage
def built_in_examples():
    sol = Solution()
    print("Built-in Examples:")
    print("Example 1: arr = [3, 2, 1], k = 2 => Output:", sol.kthLargest([3, 2, 1], 2))  # Output: 5
    print("Example 2: arr = [2, 6, 4, 1], k = 3 => Output:", sol.kthLargest([2, 6, 4, 1], 3))  # Output: 11

# User Input Example
def user_input_example():
    print("\nUser Input:")
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    k = int(input("Enter the value of k: "))
    sol = Solution()
    result = sol.kthLargest(arr, k)
    print("K-th Largest Sum of Contiguous Subarray is:", result)

# Run both
if __name__ == "__main__":
    built_in_examples()
    user_input_example()
