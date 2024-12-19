# Kth Missing Positive Number in a Sorted Array
def findKthMissing(arr, k):
    # Initialize the variable for the current number and the missing count
    missing_count = 0
    current_num = 1
    i = 0
    n = len(arr)
    
    # Loop until we find the kth missing number
    while missing_count < k:
        # If we haven't exhausted the array and the current number is equal to arr[i], move to the next element in arr
        if i < n and arr[i] == current_num:
            i += 1
        else:
            # If current_num is missing, increment the missing count
            missing_count += 1
            if missing_count == k:
                return current_num
        # Move to the next number
        current_num += 1

    return current_num

# Example usage:

# Test case 1
arr1 = [2, 3, 4, 7, 11]
k1 = 5
print(f"5th missing number: {findKthMissing(arr1, k1)}")  # Output: 9

# Test case 2
arr2 = [1, 2, 3]
k2 = 2
print(f"2nd missing number: {findKthMissing(arr2, k2)}")  # Output: 5

# Test case 3
arr3 = [3, 5, 9, 10, 11, 12]
k3 = 2
print(f"2nd missing number: {findKthMissing(arr3, k3)}")  # Output: 2
