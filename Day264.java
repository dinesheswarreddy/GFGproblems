//Palindrome Sentence
import java.util.Scanner;

class Solution {
    public boolean isPalinSent(String s) {
        StringBuilder cleaned = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                cleaned.append(Character.toLowerCase(c));
            }
        }

        int left = 0, right = cleaned.length() - 1;
        while (left < right) {
            if (cleaned.charAt(left) != cleaned.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);

        // 🔹 Inbuilt test cases
        System.out.println("Inbuilt Test Cases:");
        System.out.println("\"Too hot to hoot\" -> " + sol.isPalinSent("Too hot to hoot")); // true
        System.out.println("\"Abc 012..## 10cbA\" -> " + sol.isPalinSent("Abc 012..## 10cbA")); // true
        System.out.println("\"ABC $. def01ASDF\" -> " + sol.isPalinSent("ABC $. def01ASDF")); // false
        System.out.println();

        // 🔹 User input
        System.out.print("Enter a sentence to check if it's a palindrome: ");
        String input = sc.nextLine();
        boolean result = sol.isPalinSent(input);
        System.out.println("Is palindrome sentence? " + result);
    }
}
