#Check for BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    
    def isBST(self, root):
        def is_valid_bst(node, low, high):
            if not node:
                return True
            
            if not (low < node.data < high):
                return False
            
            return (is_valid_bst(node.left, low, node.data) and
                    is_valid_bst(node.right, node.data, high))
        
        return is_valid_bst(root, float('-inf'), float('inf'))


# Example 1: Inbuilt Binary Tree
# Constructing a simple BST
#         2
#        / \
#       1   3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node2.left = node1
node2.right = node3

bst_solution = Solution()
print("Inbuilt Tree is BST:", bst_solution.isBST(node2))  # Expected: True


# Example 2: Taking Input from User
def create_tree_from_input():
    n = int(input("Enter number of nodes: "))
    if n == 0:
        return None

    nodes = {}
    for i in range(n):
        data = int(input(f"Enter data for node {i + 1}: "))
        nodes[i] = Node(data)

    for i in range(n):
        left = int(input(f"Enter left child index for node {i + 1} (enter -1 if no left child): "))
        right = int(input(f"Enter right child index for node {i + 1} (enter -1 if no right child): "))

        if left != -1:
            nodes[i].left = nodes[left]
        if right != -1:
            nodes[i].right = nodes[right]
    
    return nodes[0]  # return the root node

# Taking user input to create a tree
user_root = create_tree_from_input()
print("User-created Tree is BST:", bst_solution.isBST(user_root))
