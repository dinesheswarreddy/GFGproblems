#Rotate a Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    # Function to rotate a linked list.
    def rotate(self, head, k):
        if not head or k == 0:
            return head
        
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        current.next = head  # Make the list circular
        
        steps_to_new_head = k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        return new_head

# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example 1: Hardcoded list (Inbuilt)
values_inbuilt = [10, 20, 30, 40, 50]
k_inbuilt = 4
head_inbuilt = create_linked_list(values_inbuilt)

print("Original list:")
print_list(head_inbuilt)

solution = Solution()
new_head_inbuilt = solution.rotate(head_inbuilt, k_inbuilt)

print(f"List after rotating {k_inbuilt} times left:")
print_list(new_head_inbuilt)

# Example 2: Input from user
values_user = list(map(int, input("Enter values for the linked list (space-separated): ").split()))
k_user = int(input("Enter number of rotations (k): "))

head_user = create_linked_list(values_user)

print("Original list:")
print_list(head_user)

new_head_user = solution.rotate(head_user, k_user)

print(f"List after rotating {k_user} times left:")
print_list(new_head_user)
