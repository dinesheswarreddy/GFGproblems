#Clone List with Next and Random
# Definition for the Node class
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None


class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None
        
        # Step 1: Interleave the original list and the new list
        current = head
        while current:
            new_node = Node(current.data)  # Create a new node
            new_node.next = current.next   # Link it to the next node
            current.next = new_node        # Insert it after the current node
            current = new_node.next       # Move to the next original node
        
        # Step 2: Set the random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next  # Set the random pointer of the copied node
            current = current.next.next  # Move to the next original node
        
        # Step 3: Separate the two interleaved lists
        current = head
        new_head = head.next  # The copied list starts right after the first original node
        while current:
            copy = current.next
            current.next = copy.next  # Restore the next pointer for the original list
            if copy.next:
                copy.next = copy.next.next  # Restore the next pointer for the copied list
            current = current.next  # Move to the next original node
        
        return new_head


# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(f"Node data: {current.data}, Random points to: {current.random.data if current.random else 'None'}")
        current = current.next


# Function to create a linked list from user input
def create_linked_list_from_input():
    n = int(input("Enter the number of nodes in the linked list: "))
    if n == 0:
        return None
    
    head = None
    prev = None
    nodes = []
    
    for i in range(n):
        data = int(input(f"Enter data for node {i+1}: "))
        new_node = Node(data)
        nodes.append(new_node)
        
        if prev:
            prev.next = new_node
        else:
            head = new_node
        
        prev = new_node
    
    for i in range(n):
        random_index = input(f"Enter random index for node {i+1} (1-based index, 'None' for no random pointer): ")
        if random_index.lower() != 'none':
            random_index = int(random_index) - 1
            nodes[i].random = nodes[random_index]
    
    return head


# In-built example
def create_inbuilt_example():
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.random = node3
    node2.random = node3
    node3.random = None
    node4.random = node3

    return node1


# Main function
if __name__ == "__main__":
    # Example 1: User input
    print("Create a linked list from user input:")
    head_user_input = create_linked_list_from_input()
    solution = Solution()
    cloned_list_user_input = solution.cloneLinkedList(head_user_input)
    print("\nOriginal list (User input):")
    print_linked_list(head_user_input)
    print("\nCloned list (User input):")
    print_linked_list(cloned_list_user_input)

    # Example 2: In-built linked list
    print("\nIn-built linked list example:")
    head_inbuilt = create_inbuilt_example()
    cloned_list_inbuilt = solution.cloneLinkedList(head_inbuilt)
    print("\nOriginal list (In-built):")
    print_linked_list(head_inbuilt)
    print("\nCloned list (In-built):")
    print_linked_list(cloned_list_inbuilt)
