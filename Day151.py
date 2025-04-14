#Alien Dictionary

from collections import defaultdict, deque

class Solution:
    @staticmethod
    def findOrder(words):
        # Step 1: Create graph and in-degree map
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        # Initialize graph with all unique characters
        for word in words:
            for char in word:
                if char not in in_degree:
                    in_degree[char] = 0
        
        # Step 2: Build edges between characters from word pairs
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # Edge case: "abcd" and "ab"
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        
        # Step 3: Perform topological sort (Kahn's algorithm)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If order contains all unique letters, it's valid
        if len(order) == len(in_degree):
            return ''.join(order)
        else:
            return ""  # Cycle detected

# Helper to validate if the order is correct
def isValidOrder(order, words):
    position = {char: i for i, char in enumerate(order)}
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for a, b in zip(w1, w2):
            if position[a] < position[b]:
                break
            elif position[a] > position[b]:
                return False
        else:
            if len(w1) > len(w2):
                return False
    return True

# --------- Main Code ---------
if __name__ == "__main__":
    try:
        # Input from user
        raw_input = input("Enter words separated by space (or press Enter to use default example): ").strip()
        if raw_input:
            words = raw_input.split()
        else:
            # Default hardcoded example
            words = ["baa", "abcd", "abca", "cab", "cad"]

        print(f"Words: {words}")
        order = Solution.findOrder(words)
        if order:
            print(f"Alien Dictionary Order: {order}")
            print(f"Valid Order: {isValidOrder(order, words)}")
        else:
            print("No valid order exists. Inconsistent dictionary.")
    except Exception as e:
        print("Error:", e)
