#nCr

class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1

        C = [0] * (r + 1)
        C[0] = 1  # nC0 is always 1

        for i in range(1, n + 1):
            j = min(i, r)
            while j > 0:
                C[j] = C[j] + C[j - 1]
                j -= 1

        return C[r]

# Example usage:
if __name__ == "__main__":
    # Take input from user
    try:
        n = int(input("Enter value of n (1 ≤ n ≤ 100): "))
        r = int(input("Enter value of r (0 ≤ r ≤ 100): "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        exit(1)

    # Check constraints
    if not (1 <= n <= 100 and 0 <= r <= 100):
        print("Input out of range.")
        exit(1)

    solution = Solution()
    result = solution.nCr(n, r)

    print(f"Value of {n}C{r} is: {result}")
