#Undirected Graph Cycle
class Solution:
    def isCycle(self, V, edges):
        # Step 1: Create the adjacency list from the edges
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Step 2: Visited array to track the visited nodes
        visited = [False] * V
        
        # Step 3: DFS function to check for cycles
        def dfs(node, parent):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):  # Recur if neighbor is not visited
                        return True
                elif neighbor != parent:  # If the neighbor is visited and not the parent, it's a cycle
                    return True
            return False
        
        # Step 4: Run DFS from every node to handle disconnected graphs
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):  # Start DFS from unvisited node with no parent (-1)
                    return True
        
        # No cycle found
        return False


# Inbuilt example
solution = Solution()

# Example 1: Hardcoded (Inbuilt)
V1 = 4
E1 = 4
edges1 = [[0, 1], [0, 2], [1, 2], [2, 3]]
print("Cycle Detected (Inbuilt Example):", solution.isCycle(V1, edges1))  # Expected output: True

# Example 2: Taking input from the user
V2 = int(input("Enter number of vertices (V): "))
E2 = int(input("Enter number of edges (E): "))

edges2 = []
for _ in range(E2):
    u, v = map(int, input("Enter an edge (u, v): ").split())
    edges2.append([u, v])

print("Cycle Detected (User Input Example):", solution.isCycle(V2, edges2))
