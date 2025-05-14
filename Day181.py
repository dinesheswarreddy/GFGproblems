#Look and Say Pattern
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        result = "1"
        
        for _ in range(n - 1):
            current = ""
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1
                current += str(count) + result[i]
                i += 1
            result = current
        
        return result

# Example usage with user input
if __name__ == "__main__":
    # Take input from the user
    try:
        n = int(input("Enter the value of n (1 ≤ n ≤ 30): "))
        if 1 <= n <= 30:
            sol = Solution()
            print(f"The {n}th row of the Look-and-Say sequence is: {sol.countAndSay(n)}")
        else:
            print("Please enter a number between 1 and 30.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

    # Built-in test cases
    sol = Solution()
    print("\nBuilt-in test cases:")
    print(f"n = 3: {sol.countAndSay(3)}")  # Output: "21"
    print(f"n = 5: {sol.countAndSay(5)}")  # Output: "111221"
