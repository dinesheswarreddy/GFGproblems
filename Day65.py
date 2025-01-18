#Reverse a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Save next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev and curr one step forward
            curr = next_node
        
        return prev  # prev is the new head of the reversed list

def print_list(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("NULL")

# Example 1: Predefined linked list
# Linked list: 1 -> 2 -> 3 -> 4 -> NULL
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original list:")
print_list(head)

solution = Solution()
reversed_head = solution.reverseList(head)

print("\nReversed list:")
print_list(reversed_head)

# Example 2: Taking input from user
# Example: 5 -> 6 -> 7 -> 8 -> NULL (User input)
print("\nEnter the linked list (end with -1):")
vals = list(map(int, input().split()))

# Create linked list from user input
dummy_head = ListNode()
current = dummy_head
for val in vals:
    current.next = ListNode(val)
    current = current.next

user_input_head = dummy_head.next

print("\nOriginal list from user input:")
print_list(user_input_head)

# Reverse the list and print
reversed_user_input_head = solution.reverseList(user_input_head)

print("\nReversed list from user input:")
print_list(reversed_user_input_head)
