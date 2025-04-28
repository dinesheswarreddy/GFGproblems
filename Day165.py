#Maximum sum of Non-adjacent nodes
from collections import deque

# Node class definition
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class with max sum logic
class Solution:
    # Helper function to return a tuple (include, exclude)
    def solve(self, node):
        if node is None:
            return (0, 0)
        
        left = self.solve(node.left)
        right = self.solve(node.right)
        
        # If we include current node, we cannot include its children
        include = node.data + left[1] + right[1]
        
        # If we exclude current node, we can take max of including or excluding children
        exclude = max(left) + max(right)
        
        return (include, exclude)
    
    def getMaxSum(self, root):
        inc, exc = self.solve(root)
        return max(inc, exc)

# Helper function to build tree from level-order input
def buildTree(level_nodes):
    if not level_nodes or level_nodes[0] == 'N':
        return None

    root = Node(int(level_nodes[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(level_nodes):
        current = queue.popleft()

        # Left child
        if i < len(level_nodes) and level_nodes[i] != 'N':
            current.left = Node(int(level_nodes[i]))
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(level_nodes) and level_nodes[i] != 'N':
            current.right = Node(int(level_nodes[i]))
            queue.append(current.right)
        i += 1

    return root

# Example usage
if __name__ == "__main__":
    sol = Solution()

    # Predefined example
    predefined_input = ['1', '2', '3', '4', 'N', '5', '6']
    root1 = buildTree(predefined_input)
    print("Predefined Tree Output:", sol.getMaxSum(root1))  # Expected Output: 16

    # User input example
    user_input = input("\nEnter tree nodes in level-order (use 'N' for nulls), e.g., 1 2 3 4 N 5 6:\n")
    user_input_list = user_input.strip().split()
    root2 = buildTree(user_input_list)
    print("User Tree Output:", sol.getMaxSum(root2))
