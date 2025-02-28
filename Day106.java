//Evaluation of Postfix Expression

import java.util.Stack;
import java.util.Scanner;

class Solution {
    public int evaluate(String[] arr) {
        Stack<Integer> stack = new Stack<>();
        
        for (String s : arr) {
            if (s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/")) {
                int b = stack.pop();
                int a = stack.pop();
                
                switch (s) {
                    case "+":
                        stack.push(a + b);
                        break;
                    case "-":
                        stack.push(a - b);
                        break;
                    case "*":
                        stack.push(a * b);
                        break;
                    case "/":
                        stack.push(a / b);
                        break;
                }
            } else {
                stack.push(Integer.parseInt(s));
            }
        }
        
        return stack.pop();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Inbuilt example
        String[] inbuiltExample = {"2", "3", "1", "*", "+", "9", "-"};
        int result1 = solution.evaluate(inbuiltExample);
        System.out.println("Inbuilt Example Result: " + result1); // Output: -4
        
        // User input example
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the postfix expression (space-separated): ");
        String input = scanner.nextLine();
        String[] userInput = input.split(" ");
        int result2 = solution.evaluate(userInput);
        System.out.println("User Input Result: " + result2);
        
        scanner.close();
    }
}
