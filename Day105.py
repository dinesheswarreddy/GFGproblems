#Get Min from Stack

class Solution:
    def __init__(self):
        self.stack = []  # Main stack to hold elements
        self.min_stack = []  # Stack to hold the minimum elements

    def push(self, x):
        # Push x onto the main stack
        self.stack.append(x)
        
        # If min_stack is empty or x is smaller than or equal to the current minimum, push it to min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        # If the stack is not empty, pop the top element
        if self.stack:
            popped = self.stack.pop()
            # If the popped element is the same as the current minimum, pop it from the min_stack too
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def peek(self):
        # Return the top element from stack if it's not empty, else return -1
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self):
        # Return the top of min_stack which is the current minimum element
        if self.min_stack:
            return self.min_stack[-1]
        return -1

# Example 1: Input from user
def user_input_example():
    q = int(input("Enter number of queries: "))
    queries = []
    
    for _ in range(q):
        query = list(map(int, input().split()))
        queries.append(query)

    solution = Solution()
    result = []
    
    for query in queries:
        if query[0] == 1:  # Push operation
            solution.push(query[1])
        elif query[0] == 2:  # Pop operation
            solution.pop()
        elif query[0] == 3:  # Peek operation
            result.append(solution.peek())
        elif query[0] == 4:  # GetMin operation
            result.append(solution.getMin())

    print("Output:", result)

# Example 2: Inbuilt queries
def inbuilt_example():
    queries = [[1, 4], [1, 2], [4], [3]]
    solution = Solution()
    result = []
    
    for query in queries:
        if query[0] == 1:  # Push operation
            solution.push(query[1])
        elif query[0] == 2:  # Pop operation
            solution.pop()
        elif query[0] == 3:  # Peek operation
            result.append(solution.peek())
        elif query[0] == 4:  # GetMin operation
            result.append(solution.getMin())

    print("Output:", result)

# Run the user input example
user_input_example()  # Uncomment this line to test user input

# Or, run the inbuilt example
# inbuilt_example()  # Uncomment this line to test inbuilt queries
