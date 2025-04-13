#Clone an Undirected Graph

from collections import deque
from typing import List

# Node class as per the problem statement
class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return f"Node({self.val})"

# Solution with graph cloning method
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            copy = Node(node.val)
            old_to_new[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)

# Utility to build a graph from an adjacency list
def build_graph(adjList: List[List[int]]) -> Node:
    if not adjList:
        return None

    nodes = [Node(i) for i in range(len(adjList))]
    for idx, neighbors in enumerate(adjList):
        nodes[idx].neighbors = [nodes[n] for n in neighbors]
    return nodes[0]  # return reference to the first node

# Utility to print the graph using BFS traversal (for verification)
def print_graph(node: 'Node'):
    visited = set()
    queue = deque([node])
    result = {}
    
    while queue:
        curr = queue.popleft()
        if curr.val in visited:
            continue
        visited.add(curr.val)
        result[curr.val] = [n.val for n in curr.neighbors]
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)
    
    for k in sorted(result):
        print(f"{k}: {result[k]}")

# =============================
# Main driver function
# =============================

def main():
    choice = input("Enter '1' to use custom input or '2' to use built-in sample: ")
    
    if choice == '1':
        n = int(input("Enter number of nodes: "))
        adjList = []
        print(f"Enter adjacency list for each node (0 to {n-1}):")
        for i in range(n):
            neighbors = list(map(int, input(f"Neighbors of node {i}: ").strip().split()))
            adjList.append(neighbors)
    else:
        # Built-in example
        print("Using built-in sample: [[1, 2], [0, 2], [0, 1, 3], [2]]")
        adjList = [[1, 2], [0, 2], [0, 1, 3], [2]]

    # Build original graph
    original = build_graph(adjList)
    print("\nOriginal graph:")
    print_graph(original)

    # Clone graph
    solution = Solution()
    cloned = solution.cloneGraph(original)

    print("\nCloned graph:")
    print_graph(cloned)

if __name__ == "__main__":
    main()
