#Tree Boundary Traversal
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
        
        boundary = []
        
        def isLeaf(node):
            return node.left is None and node.right is None
        
        def addLeftBoundary(node):
            while node:
                if not isLeaf(node):
                    boundary.append(node.data)
                if node.left:
                    node = node.left
                else:
                    node = node.right
        
        def addLeafNodes(node):
            if node is None:
                return
            if isLeaf(node):
                boundary.append(node.data)
                return
            addLeafNodes(node.left)
            addLeafNodes(node.right)
        
        def addRightBoundary(node):
            temp = []
            while node:
                if not isLeaf(node):
                    temp.append(node.data)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            while temp:
                boundary.append(temp.pop())

        if not isLeaf(root):
            boundary.append(root.data)

        addLeftBoundary(root.left)
        addLeafNodes(root)
        addRightBoundary(root.right)
        
        return boundary

# Inbuilt Example
def inbuilt_example():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    sol = Solution()
    print("Inbuilt Example Output:", sol.boundaryTraversal(root))

# User Input Example
def user_input_example():
    n = int(input("Enter the number of nodes: "))
    nodes = []
    for _ in range(n):
        value = int(input(f"Enter value for node {_+1}: "))
        nodes.append(Node(value))

    # Construct a tree with the user input (this is just a simple example for illustration)
    root = nodes[0]
    root.left = nodes[1] if n > 1 else None
    root.right = nodes[2] if n > 2 else None
    root.left.left = nodes[3] if n > 3 else None
    root.left.right = nodes[4] if n > 4 else None
    root.right.left = nodes[5] if n > 5 else None
    root.right.right = nodes[6] if n > 6 else None

    sol = Solution()
    print("User Input Example Output:", sol.boundaryTraversal(root))

# Run examples
inbuilt_example()
user_input_example()
