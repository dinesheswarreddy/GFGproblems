#Pascal Triangle
class Solution:
    def nthRowOfPascalTriangle(self, n):
        MOD = 10**9 + 7
        row = [1]
        prev = 1
        for k in range(1, n):
            curr = (prev * (n - k) // k) % MOD
            row.append(curr)
            prev = curr
        return row

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Predefined example
    predefined_n = 5
    print(f"Predefined example (n = {predefined_n}): {sol.nthRowOfPascalTriangle(predefined_n)}")
    
    # User input
    try:
        user_n = int(input("Enter a positive integer (1 ≤ n ≤ 20): "))
        if 1 <= user_n <= 20:
            print(f"{user_n}th row of Pascal's Triangle: {sol.nthRowOfPascalTriangle(user_n)}")
        else:
            print("Error: Please enter an integer between 1 and 20.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
