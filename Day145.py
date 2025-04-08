#Bridge edge in a graph

from collections import defaultdict

class Solution:
    def isBridge(self, V, edges, c, d):
        # Create adjacency list excluding the edge c-d
        adj = defaultdict(list)
        for u, v in edges:
            if (u == c and v == d) or (u == d and v == c):
                continue  # skip the edge in question
            adj[u].append(v)
            adj[v].append(u)
        
        # Perform BFS to see if c and d are connected without the edge
        visited = [False] * V
        queue = []
        queue.append(c)
        visited[c] = True
        found = False
        
        while queue:
            node = queue.pop(0)
            if node == d:
                found = True
                break
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return not found

def main():
    solution = Solution()
    
    # Example 1: User Input
    print("Example 1: User Input")
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    edges = []
    print("Enter the edges (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        edges.append([u, v])
    c, d = map(int, input("Enter the edge to check (c d): ").split())
    print("Is the edge a bridge?", solution.isBridge(V, edges, c, d))
    
    # Example 2: Inbuilt Example 1
    print("\nExample 2: Inbuilt Example 1")
    V = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    c, d = 1, 2
    print("Vertices:", V)
    print("Edges:", edges)
    print("Edge to check:", (c, d))
    print("Is the edge a bridge?", solution.isBridge(V, edges, c, d))
    
    # Example 3: Inbuilt Example 2
    print("\nExample 3: Inbuilt Example 2")
    V = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    c, d = 0, 2
    print("Vertices:", V)
    print("Edges:", edges)
    print("Edge to check:", (c, d))
    print("Is the edge a bridge?", solution.isBridge(V, edges, c, d))

if __name__ == "__main__":
    main()
