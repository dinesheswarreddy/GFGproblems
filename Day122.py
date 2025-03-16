#Minimum Jumps

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If there's only one element, no jumps are needed
        if n <= 1:
            return 0
        
        # If the first element is 0, we cannot move anywhere
        if arr[0] == 0:
            return -1
        
        jumps = 1  # We start with one jump from the first element
        current_end = arr[0]  # The farthest we can reach with the current jump
        farthest = arr[0]  # The farthest we can reach with the next jump
        
        for i in range(1, n):
            # Update the farthest we can reach
            farthest = max(farthest, i + arr[i])
            
            # If we have reached the end of the range for the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest  # Update the range to the farthest we can reach
                
                # If the current_end is enough to reach or surpass the last index
                if current_end >= n - 1:
                    return jumps
            
            # If we cannot move forward from here, return -1
            if i >= farthest:
                break
        
        return -1


# Example usage

# 1. Inbuilt test case
sol = Solution()
arr_inbuilt = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(f"Inbuilt Test Case Output: {sol.minJumps(arr_inbuilt)}")  # Expected Output: 3

# 2. User input test case
arr_input = list(map(int, input("Enter the array elements (space-separated): ").split()))
print(f"User Input Test Case Output: {sol.minJumps(arr_input)}")
