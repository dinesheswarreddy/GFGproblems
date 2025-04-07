#Directed Graph Cycle

class Solution:
    def isCycle(self, V, edges):
        # Create an adjacency list from the given edges
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        
        # States for nodes: 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * V
        
        # Helper function to perform DFS and check for cycles
        def dfs(node):
            if visited[node] == 1:
                return True  # Found a cycle (node is in visiting state)
            if visited[node] == 2:
                return False  # Already fully processed node
            
            visited[node] = 1  # Mark the node as visiting
            
            for neighbor in adj[node]:
                if dfs(neighbor):  # Recurse for all neighbors
                    return True
            
            visited[node] = 2  # Mark the node as fully visited
            return False
        
        # Try to perform DFS on each node
        for i in range(V):
            if visited[i] == 0:  # If the node is unvisited
                if dfs(i):
                    return True  # Cycle detected
        
        return False  # No cycle detected

# Function to take input from the user
def take_input():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    
    edges = []
    print("Enter the edges (u, v) for each edge:")
    for _ in range(E):
        u, v = map(int, input().split())
        edges.append([u, v])
    
    return V, edges

# Example 1: Inbuilt example
def inbuilt_example():
    V = 4
    edges = [[0, 1], [1, 2], [2, 3], [3, 3]]
    sol = Solution()
    print("Inbuilt Example 1:")
    print("Cycle present?" , sol.isCycle(V, edges))

# Example 2: Another inbuilt example
def another_inbuilt_example():
    V = 3
    edges = [[0, 1], [1, 2]]
    sol = Solution()
    print("Inbuilt Example 2:")
    print("Cycle present?" , sol.isCycle(V, edges))

# Main program
if __name__ == "__main__":
    # Running inbuilt examples
    inbuilt_example()
    another_inbuilt_example()

    # Taking user input
    V, edges = take_input()
    sol = Solution()
    print("User Input Example:")
    print("Cycle present?" , sol.isCycle(V, edges))
