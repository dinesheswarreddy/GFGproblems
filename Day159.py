#Unique Number I

class Solution:
    def findUnique(self, arr):
        result = 0
        for num in arr:
            result ^= num
        return result

# Taking input from the user
if __name__ == "__main__":
    input_str = input("Enter the numbers separated by spaces: ")
    arr = list(map(int, input_str.strip().split()))
    
    solution = Solution()
    unique_number = solution.findUnique(arr)
    
    print("The number that occurs only once is:", unique_number)
    s = Solution()
    print(s.findUnique([1, 2, 1, 5, 5]))      # Output: 2
    print(s.findUnique([2, 30, 2, 15, 20, 30, 15]))  # Output: 20
