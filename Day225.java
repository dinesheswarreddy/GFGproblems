//Mobile numeric keypad

import java.util.Scanner;

public class Solution {

    public int getCount(int n) {
        if (n == 1) return 10;

        int[][] moves = {
            {0, 8},       // 0
            {1, 2, 4},    // 1
            {2, 1, 3, 5}, // 2
            {3, 2, 6},    // 3
            {4, 1, 5, 7}, // 4
            {5, 2, 4, 6, 8}, // 5
            {6, 3, 5, 9}, // 6
            {7, 4, 8},    // 7
            {8, 5, 7, 9, 0}, // 8
            {9, 6, 8}     // 9
        };

        int[][] dp = new int[n + 1][10];

        for (int d = 0; d <= 9; d++) {
            dp[1][d] = 1;
        }

        for (int len = 2; len <= n; len++) {
            for (int d = 0; d <= 9; d++) {
                for (int move : moves[d]) {
                    dp[len][d] += dp[len - 1][move];
                }
            }
        }

        int total = 0;
        for (int d = 0; d <= 9; d++) {
            total += dp[n][d];
        }

        return total;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 📥 Input from user
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the length of the sequence (1 to 15): ");
        int userInput = sc.nextInt();

        if (userInput < 1 || userInput > 15) {
            System.out.println("Invalid input. Please enter a number between 1 and 15.");
        } else {
            int result = sol.getCount(userInput);
            System.out.println("Total unique sequences of length " + userInput + " = " + result);
        }

        // 💡 Example with hardcoded input
        int exampleInput = 2;
        int exampleResult = sol.getCount(exampleInput);
        System.out.println("Example usage (n = " + exampleInput + "): " + exampleResult + " sequences");

        sc.close();
    }
}
