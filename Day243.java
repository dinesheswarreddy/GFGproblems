//Divisible by 13

import java.util.Scanner;

class Solution {
    public boolean divby13(String s) {
        int remainder = 0;

        for (int i = 0; i < s.length(); i++) {
            int digit = s.charAt(i) - '0';
            remainder = (remainder * 10 + digit) % 13;
        }

        return remainder == 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input from user
        System.out.print("Enter a large number: ");
        String number = scanner.nextLine();

        // Check divisibility
        Solution solution = new Solution();
        boolean result = solution.divby13(number);

        // Output result
        if (result) {
            System.out.println("True (The number is divisible by 13)");
        } else {
            System.out.println("False (The number is not divisible by 13)");
        }

        scanner.close();
    }
}
