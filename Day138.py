#DFS of Graph
class Solution:
    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        visited = [False] * len(adj)  # To keep track of visited nodes
        result = []  # To store the DFS traversal result
        
        # Helper function for DFS
        def dfs_util(node):
            # Mark the current node as visited
            visited[node] = True
            result.append(node)  # Add node to result

            # Recur for all the neighbors of the current node
            for neighbor in adj[node]:
                if not visited[neighbor]:  # If the neighbor has not been visited
                    dfs_util(neighbor)  # Recursively visit it

        # Start DFS from vertex 0
        dfs_util(0)
        
        return result


# Example Usage:

# Create a Solution object
sol = Solution()

# Inbuilt example:
adj1 = [[2, 3, 1], [0], [0, 4], [0], [2]]
print("Inbuilt example DFS traversal:", sol.dfs(adj1))  # Output: [0, 2, 4, 3, 1]

# User input example:
n = int(input("Enter the number of vertices in the graph: "))
adj2 = [[] for _ in range(n)]

# Getting edges as input from the user
print("Enter the adjacency list (for each vertex, enter its neighbors separated by spaces):")
for i in range(n):
    neighbors = list(map(int, input(f"Vertex {i}: ").split()))
    adj2[i] = neighbors

print("User input DFS traversal:", sol.dfs(adj2))
