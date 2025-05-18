#Level Order in spiral form

from collections import deque

# Node structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Spiral order traversal logic
class Solution:
    def findSpiral(self, root):
        if not root:
            return []
        
        result = []
        queue = deque()
        queue.append(root)
        level = 0
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if level % 2 == 0:
                result.extend(current_level[::-1])  # Even level: right to left
            else:
                result.extend(current_level)       # Odd level: left to right
                
            level += 1
            
        return result

# Function to build tree from input list
def buildTree(values):
    if not values or values[0] == "N":
        return None

    iter_vals = iter(values)
    root = Node(int(next(iter_vals)))
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        
        try:
            left_val = next(iter_vals)
            if left_val != "N":
                current.left = Node(int(left_val))
                queue.append(current.left)
                
            right_val = next(iter_vals)
            if right_val != "N":
                current.right = Node(int(right_val))
                queue.append(current.right)
        except StopIteration:
            break
            
    return root

# ---------- Main Program Starts Here ----------
if __name__ == "__main__":
    # Example 1 (Inbuilt)
    print("Example 1:")
    inbuilt_input = ["10", "20", "30", "40", "60"]
    root1 = buildTree(inbuilt_input)
    sol = Solution()
    print("Spiral Order Traversal:", sol.findSpiral(root1))

    # Example 2 (User Input)
    print("\nEnter the tree nodes in level order (use 'N' for null):")
    user_input = input("Enter space-separated values: ").strip().split()
    root2 = buildTree(user_input)
    print("Spiral Order Traversal:", sol.findSpiral(root2))
