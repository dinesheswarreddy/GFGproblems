#Count the number of possible triangles
class Solution:
    def countTriangles(self, arr):
        arr.sort()
        n = len(arr)
        count = 0

        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1

            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1

        return count


# Test cases
solution = Solution()

# Predefined example
print(solution.countTriangles([4, 6, 3, 7]))  # Output: 3

# Take input from user
user_input = input("Enter array elements separated by space: ")
user_array = list(map(int, user_input.split()))
print(solution.countTriangles(user_array))
