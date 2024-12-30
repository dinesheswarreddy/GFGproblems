#Union of Arrays with Duplicates
def union_of_arrays(a, b):
    # Create a set to store unique elements
    union_set = set()
    
    # Add all elements from both arrays to the set
    union_set.update(a)
    union_set.update(b)
    
    # The size of the set is the number of distinct elements in the union
    return len(union_set)

# Test cases
a1 = [1, 2, 3, 4, 5]
b1 = [1, 2, 3]
print(union_of_arrays(a1, b1))  # Output: 5

a2 = [85, 25, 1, 32, 54, 6]
b2 = [85, 2]
print(union_of_arrays(a2, b2))  # Output: 7

a3 = [1, 2, 1, 1, 2]
b3 = [2, 2, 1, 2, 1]
print(union_of_arrays(a3, b3))  # Output: 2
