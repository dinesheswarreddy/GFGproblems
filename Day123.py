#Subset Sum Problem


class Solution:
    def isSubsetSum(self, arr, n, sum):
        # Base cases
        if sum == 0:
            return True
        if n == 0 and sum != 0:
            return False

        # If the last element is greater than the sum, ignore it
        if arr[n-1] > sum:
            return self.isSubsetSum(arr, n-1, sum)

        # Otherwise, check if sum can be obtained by:
        # (1) including the last element or
        # (2) excluding the last element
        return self.isSubsetSum(arr, n-1, sum) or self.isSubsetSum(arr, n-1, sum-arr[n-1])

# Example 1: Inbuilt Example
print("Inbuilt Example:")
arr1 = [3, 34, 4, 12, 5, 2]
sum1 = 9
sol = Solution()
print("Result for sum 9:", sol.isSubsetSum(arr1, len(arr1), sum1))  # Output: True

# Example 2: User Input Example
print("\nUser Input Example:")
# Take input from the user
n = int(input("Enter number of elements in the array: "))
arr2 = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr2.append(num)

sum2 = int(input("Enter the target sum: "))

# Check if subset sum exists
print("Result for the given sum:", sol.isSubsetSum(arr2, len(arr2), sum2))
