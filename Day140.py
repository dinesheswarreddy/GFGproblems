#Rotten Oranges
from collections import deque

class Solution:
    def orangesRotting(self, mat):
        # Get the dimensions of the matrix
        n, m = len(mat), len(mat[0])
        
        # Directions for up, down, left, right movements
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Queue for BFS, storing (row, col)
        queue = deque()
        fresh_count = 0
        
        # Initialize the queue with all rotten oranges and count the fresh oranges
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    queue.append((i, j))  # Rotten orange found
                elif mat[i][j] == 1:
                    fresh_count += 1  # Fresh orange found
        
        # If there are no fresh oranges, return 0
        if fresh_count == 0:
            return 0
        
        time_taken = 0
        
        # BFS to propagate the rot
        while queue:
            # Process all nodes at the current level
            level_size = len(queue)
            for _ in range(level_size):
                x, y = queue.popleft()
                
                # Explore all four directions
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    # Check if the new position is within bounds and is a fresh orange
                    if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
                        # Rot the orange and add it to the queue
                        mat[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_count -= 1  # Decrease fresh orange count
            
            # After processing all nodes at the current level, increment the time
            if queue:  # If there are still elements in the queue, increment time
                time_taken += 1
        
        # If there are still fresh oranges left, return -1
        return time_taken if fresh_count == 0 else -1


# Example 1: Inbuilt Example
mat_inbuilt = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
sol = Solution()
print("Output for inbuilt example:", sol.orangesRotting(mat_inbuilt))  # Expected Output: 1

# Example 2: Taking matrix input from user
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
print("Enter the matrix row by row (0 for empty, 1 for fresh, 2 for rotten):")

mat_user = []
for i in range(n):
    row = list(map(int, input().split()))
    mat_user.append(row)

print("Output for user input example:", sol.orangesRotting(mat_user))
