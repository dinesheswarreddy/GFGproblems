#Level order traversal
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)
                level.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

# Example 1: Inbuilt tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sol = Solution()
print("Level Order Traversal (Inbuilt Tree):", sol.levelOrder(root))

# Example 2: Tree built from user input
def build_tree_from_input():
    # Take user input for tree nodes
    values = input("Enter values for the tree nodes separated by spaces: ").split()
    if not values:
        return None

    # Create the root node
    root = Node(int(values[0]))
    queue = [root]
    i = 1

    # Build the tree using BFS
    while i < len(values):
        node = queue.pop(0)

        if i < len(values):
            left_value = int(values[i])
            node.left = Node(left_value)
            queue.append(node.left)
            i += 1

        if i < len(values):
            right_value = int(values[i])
            node.right = Node(right_value)
            queue.append(node.right)
            i += 1

    return root

# Build tree from user input
root_from_input = build_tree_from_input()
if root_from_input:
    sol = Solution()
    print("Level Order Traversal (User Input Tree):", sol.levelOrder(root_from_input))
else:
    print("No tree was created.")
