#Inorder Traversal
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def inOrder(self, root):
        result = []
        
        def traverse(node):
            if node:
                traverse(node.left)     
                result.append(node.data) 
                traverse(node.right)    
        traverse(root)
        
        return result

# Inbuilt example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

sol = Solution()
print("In-order traversal of inbuilt tree:", sol.inOrder(root))

# Function to take input from user
def take_input():
    val = int(input("Enter the root node value: "))
    root = Node(val)
    
    left_val = input("Enter the left child value of {} (or press enter if no left child): ".format(val))
    if left_val:
        root.left = Node(int(left_val))
    
    right_val = input("Enter the right child value of {} (or press enter if no right child): ".format(val))
    if right_val:
        root.right = Node(int(right_val))
    
    return root

# User input example
print("Enter values for the binary tree:")
root = take_input()

sol = Solution()
print("In-order traversal of user input tree:", sol.inOrder(root))
