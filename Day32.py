#K-th element of two Arrays

class Solution:
    def kthElement(self, a, b, k):
        # Initialize pointers for both arrays
        i, j = 0, 0
        count = 0
        
        # Traverse both arrays and find the kth element
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                count += 1
                if count == k:
                    return a[i]
                i += 1
            else:
                count += 1
                if count == k:
                    return b[j]
                j += 1
        
        # If we've exhausted one array, continue with the other
        while i < len(a):
            count += 1
            if count == k:
                return a[i]
            i += 1
        
        while j < len(b):
            count += 1
            if count == k:
                return b[j]
            j += 1

# Example usage
solution = Solution()

# Test case 1
a1 = [2, 3, 6, 7, 9]
b1 = [1, 4, 8, 10]
k1 = 5
result1 = solution.kthElement(a1, b1, k1)
print(f"The {k1}th element in the combined sorted array is: {result1}")  # Output: 6

# Test case 2
a2 = [100, 112, 256, 349, 770]
b2 = [72, 86, 113, 119, 265, 445, 892]
k2 = 7
result2 = solution.kthElement(a2, b2, k2)
print(f"The {k2}th element in the combined sorted array is: {result2}")  # Output: 256
