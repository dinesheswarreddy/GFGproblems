#Floyd Warshall

class Solution:
    def floydWarshall(self, dist):
        n = len(dist)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != 10**8 and dist[k][j] != 10**8:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# 🚀 Option 1: User Input
def user_input_mode():
    n = int(input("Enter number of nodes: "))
    print(f"Enter adjacency matrix ({n} x {n}) row by row (use 100000000 to represent INF):")
    dist = []
    for i in range(n):
        row = list(map(int, input().split()))
        dist.append(row)
    
    sol = Solution()
    sol.floydWarshall(dist)
    
    print("\nShortest distances between every pair of nodes:")
    printMatrix(dist)

# ✅ Option 2: Inbuilt Example
def inbuilt_example_mode():
    dist = [
        [0, 4, 10**8, 5, 10**8],
        [10**8, 0, 1, 10**8, 6],
        [2, 10**8, 0, 3, 10**8],
        [10**8, 10**8, 1, 0, 2],
        [1, 10**8, 10**8, 4, 0]
    ]
    sol = Solution()
    sol.floydWarshall(dist)
    
    print("Inbuilt example result:")
    printMatrix(dist)

# 🧠 Choose mode
if __name__ == "__main__":
    mode = input("Choose mode (1 for user input, 2 for inbuilt example): ")
    if mode == '1':
        user_input_mode()
    else:
        inbuilt_example_mode()
