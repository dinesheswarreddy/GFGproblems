//Maximum sum of elements not part of LIS

import bisect

class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        total_sum = sum(arr)

        # ends[i] = smallest tail of all increasing subsequences with length i+1
        # sums[i] = minimum sum of subsequence of length i+1
        ends = []
        sums = []

        for num in arr:
            idx = bisect.bisect_left(ends, num)
            curr_sum = num

            if idx > 0:
                curr_sum += sums[idx - 1]

            if idx == len(ends):
                ends.append(num)
                sums.append(curr_sum)
            else:
                if curr_sum < sums[idx]:
                    ends[idx] = num
                    sums[idx] = curr_sum

        min_lis_sum = sums[-1]
        return total_sum - min_lis_sum

# ---------- Example Usage Below ----------

def run_builtin_tests():
    sol = Solution()
    print("Running built-in test cases:")
    print(f"Test 1: [4, 6, 1, 2, 3, 8] → Output: {sol.nonLisMaxSum([4, 6, 1, 2, 3, 8])} (Expected: 10)")
    print(f"Test 2: [5, 4, 3, 2, 1] → Output: {sol.nonLisMaxSum([5, 4, 3, 2, 1])} (Expected: 14)")
    print(f"Test 3: [1, 3, 2, 4, 6] → Output: {sol.nonLisMaxSum([1, 3, 2, 4, 6])} (Expected: 3)")
    print()

def run_user_input():
    print("Enter space-separated positive integers:")
    try:
        arr = list(map(int, input().strip().split()))
        sol = Solution()
        result = sol.nonLisMaxSum(arr)
        print(f"Maximum sum of elements not in LIS: {result}")
    except Exception as e:
        print(f"Invalid input. Error: {e}")

# ---------- Main ----------

if __name__ == "__main__":
    run_builtin_tests()
    run_user_input()
