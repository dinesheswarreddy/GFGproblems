//Lexicographically Largest String After K Deletions
import java.util.*;

public class Solution {
    
    public static String maxSubseq(String s, int k) {
        int n = s.length();
        int keep = n - k; // number of characters to keep
        StringBuilder stack = new StringBuilder();

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            // Remove smaller characters from the end while we can still remove characters
            while (stack.length() > 0 && 
                   stack.charAt(stack.length() - 1) < c && 
                   (stack.length() + (n - i - 1)) >= keep) {
                stack.deleteCharAt(stack.length() - 1);
            }

            if (stack.length() < keep) {
                stack.append(c);
            }
        }

        return stack.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // ---- User Input ----
        System.out.println("Enter the string:");
        String input = scanner.nextLine();

        System.out.println("Enter the number of deletions (k):");
        int k = scanner.nextInt();

        String result = maxSubseq(input, k);
        System.out.println("Lexicographically largest string: " + result);

        // ---- Built-in Examples ----
        System.out.println("\nBuilt-in test cases:");

        System.out.println("Test Case 1: s = \"ritz\", k = 2");
        System.out.println("Expected Output: tz");
        System.out.println("Actual Output: " + maxSubseq("ritz", 2));

        System.out.println("\nTest Case 2: s = \"zebra\", k = 3");
        System.out.println("Expected Output: zr");
        System.out.println("Actual Output: " + maxSubseq("zebra", 3));

        System.out.println("\nTest Case 3: s = \"abcdef\", k = 3");
        System.out.println("Expected Output: def");
        System.out.println("Actual Output: " + maxSubseq("abcdef", 3));

        scanner.close();
    }
}
