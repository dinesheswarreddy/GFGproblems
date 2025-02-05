#Mirror Tree
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def mirror(self, root):
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
        
        return root

# Example 1: Inbuilt tree
# Creating a binary tree
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

solution = Solution()
mirror_root1 = solution.mirror(root1)

# Function to print in-order traversal of the tree
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Inbuilt Example:")
inorder(mirror_root1)  # Output: 3 1 5 2 4

# Example 2: User input for tree
print("\nEnter the number of nodes:")
n = int(input())

root2 = None
for _ in range(n):
    val = int(input("Enter node value: "))
    if root2 is None:
        root2 = Node(val)
    else:
        # Example of inserting to the tree, this could be expanded
        pass

mirror_root2 = solution.mirror(root2)
print("\nUser Input Example:")
inorder(mirror_root2)
