#Intersection of Two arrays with Duplicate Elements
class Solution:
    def intersection(self, a, b):
        # Convert both arrays to sets to remove duplicates
        set_a = set(a)
        set_b = set(b)
        
        # Find the intersection of both sets
        result = set_a & set_b
        
        # Convert the result to a sorted list
        return sorted(list(result))

# Test cases
sol = Solution()
print(sol.intersection([1, 2, 1, 3, 1], [3, 1, 3, 4, 1]))  # Output: [1, 3]
print(sol.intersection([1, 1, 1], [1, 1, 1, 1, 1]))  # Output: [1]
print(sol.intersection([1, 2, 3], [4, 5, 6]))  # Output: []
