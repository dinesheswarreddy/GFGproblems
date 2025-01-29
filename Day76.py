#Implement Pow
class Solution:
    def power(self, b: float, e: int) -> float:
        # Base case: anything raised to power 0 is 1
        if e == 0:
            return 1.0
        
        # If exponent is negative, convert the problem to positive exponent by taking reciprocal of base
        if e < 0:
            b = 1 / b
            e = -e
        
        # Initialize result as 1
        result = 1.0
        
        # Exponentiation by squaring
        while e > 0:
            # If the exponent is odd, multiply the base with result
            if e % 2 == 1:
                result *= b
            
            # Square the base and halve the exponent
            b *= b
            e //= 2
        
        return result

# Example 1: Inbuilt test case
sol = Solution()
print("Inbuilt Example 1: power(3.00000, 5) =", sol.power(3.00000, 5))  # Output: 243.00000

# Example 2: Taking input from the user
b = float(input("Enter base (b): "))
e = int(input("Enter exponent (e): "))
print(f"User Input Example: power({b}, {e}) =", sol.power(b, e))
