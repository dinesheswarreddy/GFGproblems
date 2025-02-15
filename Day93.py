#Lowest Common Ancestor in a BST
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def LCA(self, root, n1, n2):
        while root:
            if n1.data < root.data and n2.data < root.data:
                root = root.left
            elif n1.data > root.data and n2.data > root.data:
                root = root.right
            else:
                return root
        return None

# Predefined Tree
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

# Take input for the second node from the user
user_input = int(input("Enter the value of the second node to find LCA: "))

# Predefined node n1 (in this case, n1 = 8)
n1 = root.left  # Node with data 8
n2 = None

# Find the node with user input value
def find_node(root, value):
    if root is None:
        return None
    if root.data == value:
        return root
    elif value < root.data:
        return find_node(root.left, value)
    else:
        return find_node(root.right, value)

# Fetch the second node based on user input
n2 = find_node(root, user_input)

# Create an instance of Solution and find LCA
ob = Solution()
lca_node = ob.LCA(root, n1, n2)

# Output the result
if lca_node:
    print(f"The Lowest Common Ancestor of {n1.data} and {n2.data} is {lca_node.data}")
else:
    print("One or both nodes not found in the tree.")
