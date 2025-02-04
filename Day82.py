#Diameter of a Binary Tree
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Solution:
    def diameter(self, root):
        def dfs(node):
            if not node:
                return 0, 0
            
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)
            
            current_height = max(left_height, right_height) + 1
            current_diameter = left_height + right_height
            max_diameter = max(left_diameter, right_diameter, current_diameter)
            
            return current_height, max_diameter
        
        _, diameter = dfs(root)
        return diameter

# Example 1: Inbuilt example
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

solution = Solution()
print("Diameter of the tree (inbuilt example):", solution.diameter(root1))

# Example 2: User input example
def build_tree_from_input():
    n = int(input("Enter the number of nodes: "))
    if n == 0:
        return None
    
    print(f"Enter the root value:")
    root_value = int(input())
    root = Node(root_value)
    nodes = {root_value: root}
    
    for _ in range(n-1):
        print(f"Enter the parent node and its left and right children values (or -1 for no child):")
        parent_val = int(input())
        left_val = int(input())
        right_val = int(input())
        
        parent_node = nodes.get(parent_val, Node(parent_val))
        if left_val != -1:
            parent_node.left = Node(left_val)
            nodes[left_val] = parent_node.left
        if right_val != -1:
            parent_node.right = Node(right_val)
            nodes[right_val] = parent_node.right
    
    return root

root2 = build_tree_from_input()
print("Diameter of the tree (user input example):", solution.diameter(root2))
