#Articulation Point - II

class Solution:
    def articulationPoints(self, V, edges):
        # Adjacency list representation of the graph
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Initialize necessary variables
        discovery = [-1] * V  # Discovery time of vertices
        low = [-1] * V  # Lowest point reachable
        parent = [-1] * V  # Parent of each node in DFS tree
        articulation_points = set()  # Set to store articulation points
        time = [0]  # To keep track of discovery time
        visited = [False] * V  # To track visited nodes
        
        # Helper DFS function
        def dfs(u):
            children = 0
            visited[u] = True
            discovery[u] = low[u] = time[0]
            time[0] += 1

            # Go through all adjacent vertices
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)

                    # After the DFS call, update the low[u] value
                    low[u] = min(low[u], low[v])

                    # Check articulation point condition
                    if parent[u] == -1 and children > 1:  # Case for root node
                        articulation_points.add(u)
                    if parent[u] != -1 and low[v] >= discovery[u]:  # Case for non-root nodes
                        articulation_points.add(u)
                
                elif v != parent[u]:  # If v is already visited and not parent
                    low[u] = min(low[u], discovery[v])

        # Run DFS for each unvisited node
        for i in range(V):
            if not visited[i]:
                dfs(i)

        # If no articulation points, return [-1]
        if not articulation_points:
            return [-1]
        
        # Convert the set to a sorted list
        return sorted(list(articulation_points))


# Function to take user input and call the solution
def main():
    # Taking user input for number of vertices and edges
    V = int(input("Enter number of vertices (V): "))
    E = int(input("Enter number of edges (E): "))

    # Taking edges as input
    edges = []
    print("Enter the edges in the format u v (space separated) for each edge:")
    for _ in range(E):
        u, v = map(int, input().split())
        edges.append([u, v])

    # Create Solution object
    solution = Solution()
    
    # Get articulation points
    result = solution.articulationPoints(V, edges)

    # Display result
    if result == [-1]:
        print("No articulation points found.")
    else:
        print("Articulation points:", result)

# Inbuilt test case example
def inbuilt_test_case():
    V = 5
    edges = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]
    solution = Solution()
    result = solution.articulationPoints(V, edges)
    print("Inbuilt Test Case - Articulation points:", result)

# Main function to run both user input and inbuilt test case
if __name__ == "__main__":
    # Inbuilt test case
    inbuilt_test_case()

    # User input test case
    main()
