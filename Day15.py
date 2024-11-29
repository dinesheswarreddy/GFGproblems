#Add Binary Strings
class Solution:
    def addBinary(self, s1: str, s2: str) -> str:
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            bit1 = int(s1[i]) if i >= 0 else 0
            bit2 = int(s2[j]) if j >= 0 else 0
            total = bit1 + bit2 + carry
            result.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1
        
        result_str = ''.join(result[::-1]).lstrip('0')
        
        return result_str if result_str else '0'

# Example Usage:
# sol = Solution()
# print(sol.addBinary("01001001", "0110101"))  # Output: "1111110"
