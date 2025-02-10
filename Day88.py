#K Sum Paths
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def sumK(self, root, k):
        prefix_map = {0: 1}
        return self.dfs(root, 0, k, prefix_map)
    
    def dfs(self, node, current_sum, k, prefix_map):
        if not node:
            return 0
        
        current_sum += node.data
        count = prefix_map.get(current_sum - k, 0)
        
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
        
        count += self.dfs(node.left, current_sum, k, prefix_map)
        count += self.dfs(node.right, current_sum, k, prefix_map)
        
        prefix_map[current_sum] -= 1
        
        return count


# Inbuilt Example:
root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(2)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.right.right = Node(11)

sol = Solution()
k = 8
print("Inbuilt Example Result:", sol.sumK(root, k))

# User Input Example:
def create_tree():
    root_val = int(input("Enter root node value: "))
    root = Node(root_val)
    
    def add_children(node):
        left_val = input(f"Enter left child of {node.data} (or 'None' for no child): ")
        if left_val != 'None':
            node.left = Node(int(left_val))
            add_children(node.left)
        
        right_val = input(f"Enter right child of {node.data} (or 'None' for no child): ")
        if right_val != 'None':
            node.right = Node(int(right_val))
            add_children(node.right)
    
    add_children(root)
    return root

user_root = create_tree()
user_k = int(input("Enter the value of k: "))
user_sol = Solution()
print("User Input Example Result:", user_sol.sumK(user_root, user_k))
