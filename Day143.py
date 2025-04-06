#Topological sort

from collections import deque

class Solution:
    
    def topoSort(self, V, edges):
        # Create adjacency list and in-degree array
        adj = [[] for _ in range(V)]
        in_degree = [0] * V
        
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        
        # Initialize a queue for nodes with zero in-degree
        queue = deque()
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
        
        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        return topo_order

def validate_topo_order(V, edges, topo_order):
    pos = {v: i for i, v in enumerate(topo_order)}
    for u, v in edges:
        if pos[u] > pos[v]:
            return False
    return True

def main():
    # Example usage with user input
    print("User Input Example:")
    V = int(input("Enter the number of vertices (V): "))
    E = int(input("Enter the number of edges (E): "))
    edges = []
    print("Enter the edges (u v) one by one:")
    for _ in range(E):
        u, v = map(int, input().split())
        edges.append([u, v])
    
    solution = Solution()
    topo_order = solution.topoSort(V, edges)
    print("Topological Order:", topo_order)
    is_valid = validate_topo_order(V, edges, topo_order)
    print("Is the topological order valid?", is_valid)
    
    # Inbuilt example
    print("\nInbuilt Example:")
    V_inbuilt = 6
    E_inbuilt = 6
    edges_inbuilt = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]
    print(f"Vertices: {V_inbuilt}, Edges: {E_inbuilt}")
    print("Edges:", edges_inbuilt)
    
    topo_order_inbuilt = solution.topoSort(V_inbuilt, edges_inbuilt)
    print("Topological Order:", topo_order_inbuilt)
    is_valid_inbuilt = validate_topo_order(V_inbuilt, edges_inbuilt, topo_order_inbuilt)
    print("Is the topological order valid?", is_valid_inbuilt)

if __name__ == "__main__":
    main()
