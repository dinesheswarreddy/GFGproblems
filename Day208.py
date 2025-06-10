//Exactly one swap

from collections import Counter

class Solution:
    def countStrings(self, s):
        n = len(s)
        freq = Counter(s)

        total_pairs = n * (n - 1) // 2  # Total i < j pairs
        same_char_pairs = sum(v * (v - 1) // 2 for v in freq.values())

        unique_strings = total_pairs - same_char_pairs

        if same_char_pairs > 0:
            unique_strings += 1  # Original string via identical character swap

        return unique_strings


if __name__ == "__main__":
    sol = Solution()

    # Example 1: Hardcoded input
    example_input = "geek"
    print(f"Example input: {example_input}")
    print(f"Distinct strings with one swap: {sol.countStrings(example_input)}\n")

    # Example 2: Take user input
    user_input = input("Enter a string to compute distinct strings after one swap: ").strip()
    result = sol.countStrings(user_input)
    print(f"Output: {result}")
