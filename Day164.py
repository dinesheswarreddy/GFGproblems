#Multiply two strings
class Solution:
    def multiplyStrings(self, s1, s2):
        # Remove leading zeros and handle negative signs
        def normalize(s):
            negative = False
            if s[0] == '-':
                negative = True
                s = s[1:]
            s = s.lstrip('0') or '0'
            return ('-' if negative else '') + s

        s1 = normalize(s1)
        s2 = normalize(s2)

        # Check for zero
        if s1 == '0' or s2 == '0':
            return '0'

        # Handle sign
        neg = (s1[0] == '-') ^ (s2[0] == '-')
        if s1[0] == '-':
            s1 = s1[1:]
        if s2[0] == '-':
            s2 = s2[1:]

        # Reverse both strings for easier calculation
        s1 = s1[::-1]
        s2 = s2[::-1]

        # Initialize result array
        res = [0] * (len(s1) + len(s2))

        # Multiply each digit
        for i in range(len(s1)):
            for j in range(len(s2)):
                res[i + j] += (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        # Remove leading zeros from the end
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        # Convert result back to string
        result = ''.join(map(str, res[::-1]))
        if neg:
            result = '-' + result
        return result


# Instantiate the Solution class
sol = Solution()

# ---------- Predefined Test Cases ----------
print("Predefined test cases:")
print('0033 * 2 =', sol.multiplyStrings("0033", "2"))      # Expected: 66
print('11 * 23 =', sol.multiplyStrings("11", "23"))        # Expected: 253
print('123 * 0 =', sol.multiplyStrings("123", "0"))        # Expected: 0
print('-33 * -2 =', sol.multiplyStrings("-33", "-2"))      # Expected: 66
print('-33 * 2 =', sol.multiplyStrings("-33", "2"))        # Expected: -66

# ---------- User Input ----------
print("\nCustom input:")
s1 = input("Enter first number as string: ")
s2 = input("Enter second number as string: ")
result = sol.multiplyStrings(s1, s2)
print(f"{s1} * {s2} = {result}")
