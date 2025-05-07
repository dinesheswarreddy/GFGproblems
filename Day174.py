#Root to Leaf Paths

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to build tree from level order input
def buildTree(s: str) -> Optional[Node]:
    if not s or s[0] == "N":
        return None

    vals = s.strip().split()
    root = Node(int(vals[0]))
    q = deque([root])
    i = 1

    while q and i < len(vals):
        current = q.popleft()

        # Left child
        if vals[i] != "N":
            current.left = Node(int(vals[i]))
            q.append(current.left)
        i += 1
        if i >= len(vals):
            break

        # Right child
        if vals[i] != "N":
            current.right = Node(int(vals[i]))
            q.append(current.right)
        i += 1

    return root

# Solution class to find all root-to-leaf paths
class Solution:
    def Paths(self, root: Optional[Node]) -> List[List[int]]:
        result = []

        def dfs(node, path):
            if not node:
                return
            path.append(node.data)
            if not node.left and not node.right:
                result.append(path[:])
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return result

# Function to print paths nicely
def printPaths(paths):
    for path in paths:
        print(path)

# ---------- Main Execution ----------
if __name__ == "__main__":
    print("Choose input method:")
    print("1. User Input")
    print("2. Use Predefined Example")
    choice = input("Enter 1 or 2: ")

    if choice.strip() == "1":
        tree_input = input("\nEnter tree elements in level-order (use 'N' for nulls):\n")
        root = buildTree(tree_input)
    else:
        print("\nUsing predefined example: [1, 2, 3, 4, 5, N, N]")
        tree_input = "1 2 3 4 5 N N"
        root = buildTree(tree_input)

    sol = Solution()
    paths = sol.Paths(root)

    print("\nRoot-to-leaf paths:")
    printPaths(paths)
