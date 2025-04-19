#Maximum XOR of two numbers in an array

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def insert(self, root, num):
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def findMaxXOR(self, root, num):
        node = root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if toggled_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children.get(bit, node)
        return max_xor

    def maxXor(self, arr):
        root = TrieNode()
        max_result = 0
        self.insert(root, arr[0])
        for num in arr[1:]:
            curr_xor = self.findMaxXOR(root, num)
            max_result = max(max_result, curr_xor)
            self.insert(root, num)
        return max_result


# === Inbuilt Example ===
sol = Solution()
inbuilt_arr = [25, 10, 2, 8, 5, 3]
print("Inbuilt Example:")
print("Array:", inbuilt_arr)
print("Maximum XOR:", sol.maxXor(inbuilt_arr))  # Output: 28

# === User Input ===
print("\nUser Input Example:")
try:
    user_input = input("Enter numbers separated by space: ")
    arr = list(map(int, user_input.strip().split()))
    if len(arr) < 2:
        print("Array must contain at least two elements.")
    else:
        print("Maximum XOR:", sol.maxXor(arr))
except Exception as e:
    print("Invalid input:", e)
