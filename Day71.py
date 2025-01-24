#Detect Loop in linked list
# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # Initialize slow and fast pointers
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1 step
            fast = fast.next.next     # Move fast pointer by 2 steps
            
            if slow == fast:          # If they meet, there is a loop
                return True
        
        # If the fast pointer reaches the end, there is no loop
        return False

# Function to create a linked list and return the head
def create_linked_list(values, loop_pos=0):
    head = None
    prev = None
    nodes = []
    
    for value in values:
        new_node = Node(value)
        if not head:
            head = new_node
        if prev:
            prev.next = new_node
        prev = new_node
        nodes.append(new_node)
    
    # Create loop if loop_pos is not 0
    if loop_pos > 0:
        last_node = nodes[-1]
        loop_node = nodes[loop_pos - 1]  # Convert to 0-based index
        last_node.next = loop_node
    
    return head

# Inbuilt example usage:
print("Inbuilt Example:")
# Creating a linked list 1 -> 2 -> 3 -> 4 with a loop at position 2
linked_list = create_linked_list([1, 2, 3, 4], loop_pos=2)
solution = Solution()
print(solution.detectLoop(linked_list))  # Output should be True (loop exists)

# User input example usage:
print("\nUser Input Example:")
# Taking input from user to create a linked list
n = int(input("Enter the number of nodes in the linked list: "))
values = []
for i in range(n):
    values.append(int(input(f"Enter value for node {i + 1}: ")))

loop_pos = int(input("Enter the position (1-based index) where the loop should start (0 if no loop): "))

user_linked_list = create_linked_list(values, loop_pos)
print("Does the linked list have a loop?", solution.detectLoop(user_linked_list))
