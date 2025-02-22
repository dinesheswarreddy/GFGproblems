//Longest valid Parentheses
import java.util.Scanner;
import java.util.Stack;

class Solution {
    static int maxLength(String s) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        int maxLen = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    maxLen = Math.max(maxLen, i - stack.peek());
                }
            }
        }
        
        return maxLen;
    }

    public static void main(String[] args) {
        // Example 1: Input from user
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string of parentheses: ");
        String userInput = sc.nextLine();
        System.out.println("Longest valid parentheses substring length: " + maxLength(userInput));
        
        // Example 2: Inbuilt string
        String inbuiltInput = ")()())";
        System.out.println("Longest valid parentheses substring length: " + maxLength(inbuiltInput));
    }
}
