#Find length of Loop

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return self.countLoopLength(slow)
        
        return 0  # No loop

    def countLoopLength(self, node_in_loop):
        count = 1
        temp = node_in_loop.next
        while temp != node_in_loop:
            count += 1
            temp = temp.next
        return count

# Helper function to build a linked list and create a loop
def build_linked_list(values, c):
    head = Node(values[0])
    current = head
    loop_node = None

    for i in range(1, len(values)):
        current.next = Node(values[i])
        current = current.next
        if i == c:
            loop_node = current

    if c != 0:
        current.next = loop_node

    return head

# Example 1: Predefined input
values = [1, 2, 3, 4, 5]
c = 2  # 0-based index; loop from node 4 to node 3
head = build_linked_list(values, c)
sol = Solution()
print("Predefined example output:", sol.countNodesInLoop(head))

# Example 2: User input
def get_user_input():
    n = int(input("Enter number of nodes: "))
    values = list(map(int, input("Enter node values separated by space: ").split()))
    c = int(input("Enter position (0-based index) to create loop (or 0 for no loop): "))
    return values, c

values, c = get_user_input()
head = build_linked_list(values, c)
print("User input example output:", sol.countNodesInLoop(head))
