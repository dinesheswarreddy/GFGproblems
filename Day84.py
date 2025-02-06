#Construct Tree from Inorder & Preorder
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, preorder):
        inorder_map = {value: idx for idx, value in enumerate(inorder)}
        self.pre_index = 0

        def build(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = preorder[self.pre_index]
            root = Node(root_val)
            self.pre_index += 1

            in_root_index = inorder_map[root_val]

            root.left = build(in_left, in_root_index - 1)
            root.right = build(in_root_index + 1, in_right)

            return root
        
        return build(0, len(inorder) - 1)

    def postOrder(self, root):
        result = []
        def postorder_helper(node):
            if not node:
                return
            postorder_helper(node.left)
            postorder_helper(node.right)
            result.append(node.data)
        
        postorder_helper(root)
        return result

# Inbuilt example
inorder = [3, 1, 4, 0, 2, 5]
preorder = [0, 1, 3, 4, 2, 5]
solution = Solution()
root = solution.buildTree(inorder, preorder)
print("Postorder traversal of the built tree (inbuilt):", solution.postOrder(root))

# User input example
inorder_input = list(map(int, input("Enter inorder traversal (space-separated): ").split()))
preorder_input = list(map(int, input("Enter preorder traversal (space-separated): ").split()))

user_solution = Solution()
user_root = user_solution.buildTree(inorder_input, preorder_input)
print("Postorder traversal of the built tree (user input):", user_solution.postOrder(user_root))
