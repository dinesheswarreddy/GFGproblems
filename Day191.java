//Sum of all substrings of a number

import java.util.Scanner;

public class Solution {

    public static int sumSubstrings(String s) {
        int n = s.length();
        long totalSum = 0;
        long prev = 0;

        for (int i = 0; i < n; i++) {
            int num = s.charAt(i) - '0';
            prev = (prev * 10 + (long)(i + 1) * num);
            totalSum += prev;
        }

        return (int) totalSum; // Guaranteed to fit in 32-bit integer
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Taking input from user
        System.out.print("Enter a number string: ");
        String userInput = scanner.nextLine();
        int userResult = sumSubstrings(userInput);
        System.out.println("Sum of all substrings (user input): " + userResult);

        // Example usage with inbuilt/hardcoded value
        String example = "6759";
        int exampleResult = sumSubstrings(example);
        System.out.println("Sum of all substrings (inbuilt example '6759'): " + exampleResult);

        scanner.close();
    }
}
