#Find the number of islands

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        # Get grid dimensions
        n = len(grid)
        m = len(grid[0])
        
        # Directions for 8 possible moves (up, down, left, right, and 4 diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def dfs(i, j):
            # If out of bounds or the cell is water, return
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 'W':
                return
            # Mark the current cell as visited by changing 'L' to 'W'
            grid[i][j] = 'W'
            # Explore all 8 directions
            for di, dj in directions:
                dfs(i + di, j + dj)
        
        island_count = 0
        # Iterate through the entire grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L':  # Found a new island
                    island_count += 1
                    dfs(i, j)  # Mark all cells of this island
        
        return island_count

# Function to take input from the user
def take_input():
    n = int(input("Enter number of rows (n): "))
    m = int(input("Enter number of columns (m): "))
    grid = []
    print("Enter the grid (each row as a space-separated string of 'L' and 'W'):")
    for i in range(n):
        row = input().split()
        grid.append(row)
    return grid

# Inbuilt Example (default grid)
inbuilt_grid = [
    ['L', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'L'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'W', 'W', 'W', 'W'],
    ['L', 'W', 'L', 'L', 'W']
]

# Creating the Solution object
sol = Solution()

# User choice for input
choice = input("Do you want to enter a custom grid? (yes/no): ").strip().lower()

if choice == 'yes':
    grid = take_input()  # Take user input
else:
    grid = inbuilt_grid  # Use inbuilt grid

# Output the result
result = sol.numIslands(grid)
print(f"Number of islands: {result}")
