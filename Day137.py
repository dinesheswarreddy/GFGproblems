#Maximize partitions in a String
class Solution:
    def maxPartitions(self, s: str) -> int:
        # Step 1: Record the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        # Step 2: Initialize variables
        partitions = 0
        current_end = 0
        for idx, char in enumerate(s):
            # Update the current end to be the maximum last occurrence of any character in the current window
            current_end = max(current_end, last_occurrence[char])
            
            # If we reach the end of a valid partition (i.e., current_end == idx)
            if idx == current_end:
                partitions += 1
        
        return partitions


# Example usage:

# Inbuilt Test Case 1
s = "ababcbacadefegdehijhklij"
solution = Solution()
print("Inbuilt Test Case 1 Result:", solution.maxPartitions(s))  # Output: 3

# Inbuilt Test Case 2
s = "acbbcc"
print("Inbuilt Test Case 2 Result:", solution.maxPartitions(s))  # Output: 2

# Inbuilt Test Case 3
s = "aaa"
print("Inbuilt Test Case 3 Result:", solution.maxPartitions(s))  # Output: 1

# User Input Test Case
user_input = input("Enter a string to partition: ")
solution = Solution()
print("User Input Test Case Result:", solution.maxPartitions(user_input))
