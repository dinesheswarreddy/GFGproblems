#Smallest distinct window
class Solution:
    def findSubString(self, str):
        n = len(str)
        if n == 0:
            return 0

        # Step 1: Count all distinct characters in the input string
        total_distinct = len(set(str))

        # Step 2: Initialize sliding window and frequency map
        freq_map = {}
        min_len = n + 1
        start = 0
        count = 0  # count of distinct characters in current window

        for end in range(n):
            # Add current character to frequency map
            freq_map[str[end]] = freq_map.get(str[end], 0) + 1

            # If this character's count is 1, we included a new unique char
            if freq_map[str[end]] == 1:
                count += 1

            # If current window has all distinct characters
            while count == total_distinct:
                window_len = end - start + 1
                if window_len < min_len:
                    min_len = window_len

                # Shrink window from left
                freq_map[str[start]] -= 1
                if freq_map[str[start]] == 0:
                    count -= 1
                start += 1

        return min_len
class Solution:
    def findSubString(self, str):
        n = len(str)
        if n == 0:
            return 0

        # Step 1: Count all distinct characters
        total_distinct = len(set(str))

        # Step 2: Sliding window initialization
        freq_map = {}
        min_len = n + 1
        start = 0
        count = 0  # count of distinct chars in current window

        for end in range(n):
            freq_map[str[end]] = freq_map.get(str[end], 0) + 1

            if freq_map[str[end]] == 1:
                count += 1

            while count == total_distinct:
                window_len = end - start + 1
                if window_len < min_len:
                    min_len = window_len

                freq_map[str[start]] -= 1
                if freq_map[str[start]] == 0:
                    count -= 1
                start += 1

        return min_len


# =======================
# User-Defined Test Cases
# =======================
sol = Solution()

# Problem-provided test cases
print("Test 1: 'aabcbcdbca' =>", sol.findSubString("aabcbcdbca"))     # Expected: 4
print("Test 2: 'aaab' =>", sol.findSubString("aaab"))                 # Expected: 2
print("Test 3: 'geeksforgeeks' =>", sol.findSubString("geeksforgeeks"))  # Expected: 8

# Custom test cases
print("Test 4: 'aaaaaaa' =>", sol.findSubString("aaaaaaa"))           # Expected: 1
print("Test 5: 'abcabcbb' =>", sol.findSubString("abcabcbb"))         # Expected: 3
print("Test 6: 'xyzzyx' =>", sol.findSubString("xyzzyx"))             # Expected: 3
print("Test 7: 'a' =>", sol.findSubString("a"))                       # Expected: 1
print("Test 8: 'abac' =>", sol.findSubString("abac"))                 # Expected: 3
print("Test 9: 'abcdeabcd' =>", sol.findSubString("abcdeabcd"))       # Expected: 5
