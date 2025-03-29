#Job Sequencing Problem

class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        jobs = sorted(zip(deadline, profit), key=lambda x: -x[1])
        
        max_deadline = max(deadline) if n > 0 else 0
        parent = [i for i in range(max_deadline + 2)]
        
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root != v_root:
                parent[v_root] = u_root
        
        count = 0
        total_profit = 0
        
        for d, p in jobs:
            available_slot = find(d)
            if available_slot > 0:
                union(available_slot - 1, available_slot)
                count += 1
                total_profit += p
        
        return [count, total_profit]

# Example usage:

# Take input from the user
n = int(input("Enter the number of jobs: "))

deadlines = []
profits = []

for i in range(n):
    deadline = int(input(f"Enter the deadline for job {i+1}: "))
    profit = int(input(f"Enter the profit for job {i+1}: "))
    deadlines.append(deadline)
    profits.append(profit)

# Initialize Solution class
solution = Solution()

# Get the result
result = solution.jobSequencing(deadlines, profits)

# Output the result
print(f"Maximum number of jobs that can be done: {result[0]}")
print(f"Maximum profit: {result[1]}")

# Inbuilt example
print("\nInbuilt Example:")
deadlines = [4, 1, 1, 1, 2]
profits = [20, 10, 40, 30, 50]
result = solution.jobSequencing(deadlines, profits)
print(f"Maximum number of jobs that can be done: {result[0]}")
print(f"Maximum profit: {result[1]}")
