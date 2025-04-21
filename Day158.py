#Missing in Array

class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        total_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return total_sum - actual_sum

# Example usage:
if __name__ == "__main__":
    # Take input from user
    input_str = input("Enter the array elements separated by spaces: ")
    arr = list(map(int, input_str.strip().split()))
    
    sol = Solution()
    missing = sol.missingNum(arr)
    print("Missing number is:", missing)
#Enter the array elements separated by spaces: 1 2 3 5
#Missing number is: 4
