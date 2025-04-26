#Is Binary Tree Heap
from collections import deque

# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Tree builder from level-order list
def buildTree(level_order):
    if not level_order or level_order[0] == 'N':
        return None

    root = Node(int(level_order[0]))
    q = deque([root])
    i = 1

    while q and i < len(level_order):
        curr = q.popleft()

        # Left child
        if level_order[i] != 'N':
            curr.left = Node(int(level_order[i]))
            q.append(curr.left)
        i += 1

        if i >= len(level_order):
            break

        # Right child
        if level_order[i] != 'N':
            curr.right = Node(int(level_order[i]))
            q.append(curr.right)
        i += 1

    return root

# Your Solution class
class Solution:
    def isHeap(self, root):
        q = deque()
        q.append(root)
        null_seen = False

        while q:
            node = q.popleft()

            if node.left:
                if null_seen or node.left.data > node.data:
                    return False
                q.append(node.left)
            else:
                null_seen = True

            if node.right:
                if null_seen or node.right.data > node.data:
                    return False
                q.append(node.right)
            else:
                null_seen = True

        return True

# ----------------- Main Execution -----------------

if __name__ == "__main__":
    sol = Solution()

    # 1️⃣ Predefined example
    predefined = ["97", "46", "37", "12", "3", "7", "31", "6", "9"]
    root1 = buildTree(predefined)
    print("Predefined Example 1:", sol.isHeap(root1))  # True

    predefined2 = ["97", "46", "37", "12", "3", "7", "31", "N", "2", "4"]
    root2 = buildTree(predefined2)
    print("Predefined Example 2:", sol.isHeap(root2))  # False

    # 2️⃣ User input
    print("\nEnter your own tree in level-order (use 'N' for nulls):")
    user_input = input().strip().split()
    root_user = buildTree(user_input)
    print("User Input Result:", sol.isHeap(root_user))
