#Fixing Two nodes of a BST
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def correctBST(self, root):
        self.first = None
        self.second = None
        self.prev = None
        
        # Helper function to perform inorder traversal
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            # Detect swapped nodes
            if self.prev and self.prev.data > node.data:
                if not self.first:
                    self.first = self.prev
                self.second = node
            
            self.prev = node
            
            inorder(node.right)
        
        # Perform inorder traversal
        inorder(root)
        
        # If swapped nodes are found, swap their values
        if self.first and self.second:
            self.first.data, self.second.data = self.second.data, self.first.data

# Function to take input from user and create a BST
def take_input():
    n = int(input("Enter the number of nodes: "))
    nodes = [int(input(f"Enter value for node {i+1}: ")) for i in range(n)]
    
    if n == 0:
        return None

    # Create the root node
    root = Node(nodes[0])
    for value in nodes[1:]:
        current = root
        while True:
            if value < current.data:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right
    return root

# Function for inorder traversal to display tree
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

# Main code to demonstrate both the inbuilt and user input cases

# Inbuilt Tree Example
print("Inbuilt Tree Example:")
root = Node(10)
root.left = Node(5)
root.right = Node(3)  # This should have been 15
root.left.left = Node(2)
root.left.right = Node(8)
root.right.left = Node(12)  # This should have been 7

# Display the tree before correction
print("Before correction (Inorder Traversal):")
inorder_traversal(root)
print()

# Correct the BST
solution = Solution()
solution.correctBST(root)

# Display the tree after correction
print("After correction (Inorder Traversal):")
inorder_traversal(root)
print()

# User Input Example
print("\nUser Input Example:")
user_root = take_input()

# Display the tree before correction
print("Before correction (Inorder Traversal):")
inorder_traversal(user_root)
print()

# Correct the BST
solution.correctBST(user_root)

# Display the tree after correction
print("After correction (Inorder Traversal):")
inorder_traversal(user_root)
print()
