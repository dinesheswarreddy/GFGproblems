#Bitonic Point

class Solution:
    def findMaximum(self, arr):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is the bitonic point
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
                return arr[mid]
            elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1


# Function to run predefined and user test cases
def run_tests():
    sol = Solution()

    # Predefined test cases
    print("Predefined Test Cases:")
    print("Max in [1, 2, 4, 5, 7, 8, 3]:", sol.findMaximum([1, 2, 4, 5, 7, 8, 3]))
    print("Max in [10, 20, 30, 40, 50]:", sol.findMaximum([10, 20, 30, 40, 50]))
    print("Max in [120, 100, 80, 20, 0]:", sol.findMaximum([120, 100, 80, 20, 0]))

    # User input test case
    print("\nUser Input Test Case:")
    try:
        user_input = input("Enter the array elements separated by space: ")
        user_array = list(map(int, user_input.strip().split()))
        print("Maximum element (bitonic point):", sol.findMaximum(user_array))
    except Exception as e:
        print("Invalid input. Please enter space-separated integers.")


# Run the tests
if __name__ == "__main__":
    run_tests()
