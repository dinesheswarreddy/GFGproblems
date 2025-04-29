#Sort a linked list of 0s, 1s and 2s

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Solution class with segregate method
class Solution:
    def segregate(self, head):
        # Step 1: Count the number of 0s, 1s, and 2s
        count = [0, 0, 0]
        current = head
        while current:
            count[current.data] += 1
            current = current.next

        # Step 2: Rewrite the list using the counts
        current = head
        i = 0
        while current:
            if count[i] == 0:
                i += 1
            else:
                current.data = i
                count[i] -= 1
                current = current.next

        return head

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.data, end=" → " if head.next else "\n")
        head = head.next

# --- Example 1: Predefined test case ---
print("Predefined Example:")
predefined_values = [1, 2, 2, 1, 2, 0, 2, 2]
head1 = create_linked_list(predefined_values)
print("Original list:")
print_linked_list(head1)
sol = Solution()
sorted_head1 = sol.segregate(head1)
print("Sorted list:")
print_linked_list(sorted_head1)

# --- Example 2: User input ---
print("\nUser Input Example:")
user_input = input("Enter space-separated values (0, 1, 2 only): ").strip()
user_values = list(map(int, user_input.split()))
head2 = create_linked_list(user_values)
print("Original list:")
print_linked_list(head2)
sorted_head2 = sol.segregate(head2)
print("Sorted list:")
print_linked_list(sorted_head2)
