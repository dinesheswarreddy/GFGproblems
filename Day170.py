#Prime List
from bisect import bisect_left

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def primeList(self, head):
        MAX = 10000 + 100  # slightly over the max node value

        # Step 1: Generate all primes using Sieve of Eratosthenes
        is_prime = [True] * (MAX + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAX ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX + 1, i):
                    is_prime[j] = False

        primes = [i for i, val in enumerate(is_prime) if val]

        # Step 2: Helper to find nearest prime to a number
        def nearest_prime(n):
            if is_prime[n]:
                return n
            idx = bisect_left(primes, n)
            # check neighbors
            before = primes[idx - 1] if idx > 0 else float('inf')
            after = primes[idx] if idx < len(primes) else float('inf')
            if abs(n - before) <= abs(after - n):
                return before
            return after

        # Step 3: Traverse and update linked list
        curr = head
        while curr:
            curr.val = nearest_prime(curr.val)
            curr = curr.next

        return head
# Utility function to build a linked list from a list
def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

# Utility function to print a linked list
def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# =======================
# User-Defined Test Cases
# =======================
sol = Solution()

# Test Case 1: Example from problem
print("Test Case 1: [1, 15, 20]")
head1 = build_linked_list([1, 15, 20])
print_list(sol.primeList(head1))  # Output: 2 -> 13 -> 19

# Test Case 2: All primes already
print("Test Case 2: [2, 3, 5, 7, 11]")
head2 = build_linked_list([2, 3, 5, 7, 11])
print_list(sol.primeList(head2))  # Output: 2 -> 3 -> 5 -> 7 -> 11

# Test Case 3: Mixed values
print("Test Case 3: [4, 6, 8, 10, 12]")
head3 = build_linked_list([4, 6, 8, 10, 12])
print_list(sol.primeList(head3))  # Output: 3 -> 5 -> 7 -> 11 -> 11

# Test Case 4: Includes large values
print("Test Case 4: [100, 9999, 10000]")
head4 = build_linked_list([100, 9999, 10000])
print_list(sol.primeList(head4))  # Output will be nearest primes

# Test Case 5: Single node
print("Test Case 5: [1]")
head5 = build_linked_list([1])
print_list(sol.primeList(head5))  # Output: 2
