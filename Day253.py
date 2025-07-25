#Max Circular Subarray Sum

class Solution:
    def maxSum(self, nums):
        positive_nums = {num for num in nums if num > 0}
        if not positive_nums:
            return max(nums)
        return sum(positive_nums)

    def maxCircularSum(self, arr):
        def kadane(arr):
            max_ending_here = max_so_far = arr[0]
            for num in arr[1:]:
                max_ending_here = max(num, max_ending_here + num)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        max_kadane = kadane(arr)
        total_sum = sum(arr)
        inverted_arr = [-num for num in arr]
        max_inverted_kadane = kadane(inverted_arr)
        max_wrap = total_sum + max_inverted_kadane

        if max_wrap == 0:
            return max_kadane
        return max(max_kadane, max_wrap)


def main():
    solution = Solution()

    # Inbuilt example usage
    example = [8, -1, 3, 4]
    print("Inbuilt Example Array:", example)
    print("maxSum (unique positive):", solution.maxSum(example))
    print("maxCircularSum:", solution.maxCircularSum(example))
    print("-" * 50)

    # User input
    user_input = input("Enter numbers separated by space: ")
    try:
        arr = list(map(int, user_input.strip().split()))
        print("User Input Array:", arr)
        print("maxSum (unique positive):", solution.maxSum(arr))
        print("maxCircularSum:", solution.maxCircularSum(arr))
    except ValueError:
        print("Invalid input! Please enter integers separated by space.")

if __name__ == "__main__":
    main()
