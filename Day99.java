//Parenthesis Checker
import java.util.Scanner;
import java.util.Stack;

class Solution {
    // Method to check if the given string has balanced parentheses
    static boolean isBalanced(String s) {
        // Stack to hold the opening brackets
        Stack<Character> stack = new Stack<>();
        
        // Traverse through the string
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            
            // If it's an opening bracket, push it onto the stack
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }
            // If it's a closing bracket, check for matching pair
            else if (ch == ')' || ch == '}' || ch == ']') {
                // If the stack is empty or top of the stack doesn't match, return false
                if (stack.isEmpty()) {
                    return false;
                }
                
                char top = stack.pop();
                
                // Check if the popped character matches the current closing bracket
                if (ch == ')' && top != '(') {
                    return false;
                }
                if (ch == '}' && top != '{') {
                    return false;
                }
                if (ch == ']' && top != '[') {
                    return false;
                }
            }
        }
        
        // If stack is empty, it means all the brackets matched correctly
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        // Example 1: Hardcoded input (Inbuilt)
        String example1 = "[{()}]";
        System.out.println("Example 1: " + example1);
        System.out.println("Is balanced? " + isBalanced(example1));

        // Example 2: Taking input from the user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string of parentheses: ");
        String userInput = scanner.nextLine();
        System.out.println("User input: " + userInput);
        System.out.println("Is balanced? " + isBalanced(userInput));
        
        scanner.close();
    }
}
