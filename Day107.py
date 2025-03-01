//Decode the string

class Solution:
    def decodedString(self, s):
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else:
                current_string += char
        
        return current_string

# Example 1: Inbuilt test case
solution = Solution()
encoded_string = "3[b2[ca]]"
print(f"Decoded string for '{encoded_string}': {solution.decodedString(encoded_string)}")

# Example 2: Input from user
user_input = input("Enter an encoded string: ")
print(f"Decoded string for '{user_input}': {solution.decodedString(user_input)}")
