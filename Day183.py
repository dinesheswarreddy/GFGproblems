#Smallest range in K lists

import heapq

class Solution:
    def findSmallestRange(self, arr):
        k = len(arr)
        n = len(arr[0])

        # Min heap: (value, row index, col index)
        heap = []
        max_val = float('-inf')

        # Initialize heap
        for i in range(k):
            val = arr[i][0]
            heapq.heappush(heap, (val, i, 0))
            max_val = max(max_val, val)

        best_range = [float('-inf'), float('inf')]

        while True:
            min_val, row, col = heapq.heappop(heap)

            # Update best range
            if max_val - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, max_val]

            # If this row is exhausted, stop
            if col + 1 == len(arr[row]):
                break

            # Push next element from the same row
            next_val = arr[row][col + 1]
            heapq.heappush(heap, (next_val, row, col + 1))
            max_val = max(max_val, next_val)

        return best_range


if __name__ == "__main__":
    sol = Solution()

    # Inbuilt example
    arr_inbuilt = [[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]
    print("Inbuilt input:", arr_inbuilt)
    print("Smallest range from inbuilt input:", sol.findSmallestRange(arr_inbuilt))

    # User input
    print("\n--- User Input ---")
    k = int(input("Enter number of lists (k): "))
    n = int(input("Enter number of elements in each list (n): "))
    arr_user = []

    print("Enter the elements of each list (space-separated):")
    for i in range(k):
        row = list(map(int, input(f"List {i+1}: ").split()))
        if len(row) != n:
            print(f"List {i+1} must have {n} elements. Please re-run and try again.")
            exit()
        arr_user.append(sorted(row))  # Sorting to ensure sorted input

    print("Smallest range from user input:", sol.findSmallestRange(arr_user))
