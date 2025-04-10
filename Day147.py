#Minimum cost to connect all houses in a city
import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        in_mst = [False] * n
        minDist = [float('inf')] * n
        minDist[0] = 0
        heap = [(0, 0)]  # (cost, node)
        total_cost = 0

        while heap:
            cost, u = heapq.heappop(heap)
            if in_mst[u]:
                continue
            in_mst[u] = True
            total_cost += cost

            for v in range(n):
                if not in_mst[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if dist < minDist[v]:
                        minDist[v] = dist
                        heapq.heappush(heap, (dist, v))

        return total_cost

# ----------- Example usage -------------

def run_examples():
    obj = Solution()

    print("Example 1 (Hardcoded):")
    houses1 = [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]]
    print("Input:", houses1)
    print("Minimum Cost:", obj.minCost(houses1))  # Expected: 105

    print("\nExample 2 (Hardcoded):")
    houses2 = [[0, 0], [1, 1], [1, 3], [3, 0]]
    print("Input:", houses2)
    print("Minimum Cost:", obj.minCost(houses2))  # Expected: 7

# ----------- User Input --------------

def run_user_input():
    obj = Solution()
    n = int(input("Enter number of houses: "))
    houses = []
    print("Enter coordinates as 'x y' (without quotes):")
    for _ in range(n):
        x, y = map(int, input().split())
        houses.append([x, y])
    print("Minimum Cost to Connect All Houses:", obj.minCost(houses))

# ---------- Choose Run Mode -------------

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Run Examples")
    print("2. Enter Custom Input")
    mode = input("Enter 1 or 2: ").strip()

    if mode == "1":
        run_examples()
    elif mode == "2":
        run_user_input()
    else:
        print("Invalid input. Exiting.")
