#Left View of Binary Tree

from collections import deque

# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to build tree from level-order input (list with N or None as null)
def build_tree(level_order):
    if not level_order or level_order[0] in ['N', None]:
        return None

    root = Node(int(level_order[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        current = queue.popleft()

        # Left child
        if i < len(level_order) and level_order[i] not in ['N', None]:
            current.left = Node(int(level_order[i]))
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(level_order) and level_order[i] not in ['N', None]:
            current.right = Node(int(level_order[i]))
            queue.append(current.right)
        i += 1

    return root

# Solution class for Left View
class Solution:
    def LeftView(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)

                if i == 0:
                    result.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

# -------------------
# Example usage
# -------------------

# Predefined input
predefined_input = [1, 2, 3, 4, 5, 'N', 'N']
root1 = build_tree(predefined_input)
sol = Solution()
print("Left view of predefined tree:", sol.LeftView(root1))

# User input
user_input = input("Enter tree in level order (use N for null), separated by space: ").split()
root2 = build_tree(user_input)
print("Left view of your tree:", sol.LeftView(root2))
