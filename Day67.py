#Merge two sorted linked lists
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def mergeTwoLists(self, head1: Node, head2: Node) -> Node:
        newNode = Node(0)
        tail = newNode
        
        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        
        if head1:
            tail.next = head1
        else:
            tail.next = head2
        
        return newNode.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    head = None
    tail = None
    for value in values:
        new_node = Node(value)
        if not head:
            head = new_node
            tail = head
        else:
            tail.next = new_node
            tail = tail.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.data, end=" -> " if head.next else "")
        head = head.next
    print()

# Example Usage
if __name__ == "__main__":
    # List 1: User input
    user_input = input("Enter the elements of the first list (comma-separated): ")
    list1_values = list(map(int, user_input.split(',')))
    head1 = create_linked_list(list1_values)

    # List 2: Predefined list
    list2_values = [1, 4, 5, 6]
    head2 = create_linked_list(list2_values)

    # Merge both lists
    solution = Solution()
    merged_head = solution.mergeTwoLists(head1, head2)

    # Print the merged linked list
    print("Merged linked list:")
    print_linked_list(merged_head)
