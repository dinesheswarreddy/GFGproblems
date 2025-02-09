#Maximum path sum from any node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findMaxSumUtil(self, root, max_sum):
        if root is None:
            return 0
        
        left = max(0, self.findMaxSumUtil(root.left, max_sum))
        right = max(0, self.findMaxSumUtil(root.right, max_sum))
        
        current_max = root.data + left + right
        max_sum[0] = max(max_sum[0], current_max)
        
        return root.data + max(left, right)
    
    def findMaxSum(self, root):
        max_sum = [-float('inf')]
        self.findMaxSumUtil(root, max_sum)
        return max_sum[0]


# Inbuilt Example:
root_inbuilt = Node(10)
root_inbuilt.left = Node(2)
root_inbuilt.right = Node(10)
root_inbuilt.left.left = Node(20)
root_inbuilt.left.right = Node(1)
root_inbuilt.right.left = None
root_inbuilt.right.right = Node(-25)
root_inbuilt.right.right.left = Node(3)
root_inbuilt.right.right.right = Node(4)

sol = Solution()
print("Inbuilt Example Max Path Sum:", sol.findMaxSum(root_inbuilt))  # Output: 42


# User Input Example:
def build_tree_from_input():
    nodes = list(map(int, input("Enter the nodes of the tree (comma separated): ").split(',')))
    
    def create_node(index):
        if index < len(nodes) and nodes[index] != 'N':
            node = Node(nodes[index])
            node.left = create_node(2 * index + 1)
            node.right = create_node(2 * index + 2)
            return node
        return None
    
    return create_node(0)

root_user_input = build_tree_from_input()
print("User Input Example Max Path Sum:", sol.findMaxSum(root_user_input))
