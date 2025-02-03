#Height of Binary Tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def height(self, root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)

# Inbuilt example:
root_inbuilt = Node(1)
root_inbuilt.left = Node(2)
root_inbuilt.right = Node(3)
root_inbuilt.left.left = Node(4)
root_inbuilt.left.right = Node(5)

solution = Solution()
print("Height of inbuilt tree:", solution.height(root_inbuilt))  # Output: 2

# Input-based example:
def build_tree():
    root_data = int(input("Enter the root node value: "))
    root = Node(root_data)
    
    def add_children(node):
        left_data = int(input(f"Enter the left child of {node.data} (or -1 if no child): "))
        if left_data != -1:
            node.left = Node(left_data)
            add_children(node.left)
        
        right_data = int(input(f"Enter the right child of {node.data} (or -1 if no child): "))
        if right_data != -1:
            node.right = Node(right_data)
            add_children(node.right)
    
    add_children(root)
    return root

root_user = build_tree()
print("Height of user-defined tree:", solution.height(root_user))
