#Substrings with same first and last characters

class Solution:
    def countSubstring(self, s):
        from collections import Counter
        
        freq = Counter(s)
        count = 0
        
        for c in freq:
            n = freq[c]
            count += n * (n + 1) // 2
        
        return count

# --- Main Code ---

if __name__ == "__main__":
    sol = Solution()

    # Option 1: Take input from the user
    s = input("Enter a lowercase string: ")
    print("Count of substrings starting and ending with same character:", sol.countSubstring(s))

    # Option 2: Built-in examples (uncomment to test)
    # examples = ["abcab", "aba", "aaaa"]
    # for example in examples:
    #     print(f"Input: {example} => Output: {sol.countSubstring(example)}")
