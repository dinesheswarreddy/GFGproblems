#Longest Subarray with Majority Greater than K

class Solution:
    def longestSubarray(self, arr, k):
        balance = 0
        prefix_map = {0: -1}  # Maps prefix_sum -> first index
        max_len = 0
        
        for i in range(len(arr)):
            if arr[i] > k:
                balance += 1
            else:
                balance -= 1

            if balance > 0:
                max_len = i + 1
            else:
                if (balance - 1) in prefix_map:
                    max_len = max(max_len, i - prefix_map[balance - 1])

            if balance not in prefix_map:
                prefix_map[balance] = i

        return max_len

# Example usage
if __name__ == "__main__":
    # User input
    arr_input = input("Enter the array elements (space-separated): ")
    arr = list(map(int, arr_input.strip().split()))
    k = int(input("Enter the value of k: "))

    # Create Solution object
    sol = Solution()
    result = sol.longestSubarray(arr, k)
    
    # Output the result
    print("Length of the longest subarray:", result)
