#Unique Number 3
class Solution:
    def getSingle(self, arr):
        ones, twos = 0, 0
        for num in arr:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones


# ---------- Example Usage ----------

def main():
    print("Choose input method:")
    print("1. Enter your own array")
    print("2. Use built-in example")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        arr = list(map(int, input("Enter space-separated integers: ").split()))
    else:
        # Example: only one element appears once
        arr = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]

    sol = Solution()
    result = sol.getSingle(arr)
    print(f"The element that appears only once is: {result}")


if __name__ == "__main__":
    main()
