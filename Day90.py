#k-th Smallest in BST
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def kthSmallest(self, root, k): 
        def in_order(node):
            if node is None:
                return []
            return in_order(node.left) + [node.data] + in_order(node.right)
        
        elements = in_order(root)
        
        if k <= len(elements):
            return elements[k - 1]
        return -1


# Inbuilt example
root1 = Node(20)
root1.left = Node(8)
root1.right = Node(22)
root1.left.left = Node(4)
root1.left.right = Node(12)
root1.left.right.left = Node(10)
root1.left.right.right = Node(14)

sol = Solution()
print("Inbuilt example - 3rd smallest:", sol.kthSmallest(root1, 3))  # Output: 10


# User input example
def build_bst_from_input():
    root = None
    n = int(input("Enter the number of nodes: "))
    for _ in range(n):
        value = int(input("Enter node value: "))
        root = insert_bst(root, value)
    return root

def insert_bst(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

root2 = build_bst_from_input()
k = int(input("Enter the value of k: "))
print(f"User input example - {k}th smallest:", sol.kthSmallest(root2, k))
