#BFS of graph

from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # Number of vertices
        V = len(adj)
        
        # List to store BFS traversal
        result = []
        
        # Visited array to track visited nodes
        visited = [False] * V
        
        # Queue for BFS
        queue = deque()
        
        # Start BFS from vertex 0
        visited[0] = True
        queue.append(0)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            # Visit all unvisited neighbors of the current node
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result


# Example usage with inbuilt test case
solution = Solution()

# Inbuilt example
adj_inbuilt = [[2, 3, 1], [0], [0, 4], [0], [2]]
print("BFS Traversal (Inbuilt Example):", solution.bfs(adj_inbuilt))

# Example usage by taking user input
V = int(input("Enter number of vertices: "))
adj_user = []
print("Enter the adjacency list:")
for i in range(V):
    neighbors = list(map(int, input(f"Enter neighbors for vertex {i} (separated by space): ").split()))
    adj_user.append(neighbors)

print("BFS Traversal (User Input Example):", solution.bfs(adj_user))
