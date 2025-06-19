//Case-specific Sorting of Strings

import java.util.*;

public class Solution {

    public static String caseSort(String s) {
        char[] chars = s.toCharArray();
        List<Character> lower = new ArrayList<>();
        List<Character> upper = new ArrayList<>();

        // Separate characters by case
        for (char c : chars) {
            if (Character.isLowerCase(c)) {
                lower.add(c);
            } else {
                upper.add(c);
            }
        }

        // Sort both lists
        Collections.sort(lower);
        Collections.sort(upper);

        // Reconstruct the result string
        StringBuilder result = new StringBuilder();
        int l = 0, u = 0;
        for (char c : chars) {
            if (Character.isLowerCase(c)) {
                result.append(lower.get(l++));
            } else {
                result.append(upper.get(u++));
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Example 1: Input from user
        System.out.print("Enter a string (only uppercase and lowercase letters): ");
        String userInput = scanner.nextLine();
        System.out.println("Sorted (case-specific): " + caseSort(userInput));

        // Example 2: Inbuilt example
        String exampleInput = "GEekS";
        System.out.println("\nExample Input: " + exampleInput);
        System.out.println("Expected Output: EGekS");
        System.out.println("Actual Output:   " + caseSort(exampleInput));

        scanner.close();
    }
}
