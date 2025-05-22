//Minimum Deletions
import java.util.Scanner;

class Solution {
    static int minDeletions(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];

        // Each single character is a palindrome of length 1
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }

        // Fill DP table
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = 2 + dp[i + 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }

        int lps = dp[0][n - 1];
        return n - lps;  // Minimum deletions
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Inbuilt test case
        String test = "aebcbda";
        System.out.println("Inbuilt test case: " + test);
        System.out.println("Minimum deletions: " + minDeletions(test));
        System.out.println();

        // User input
        System.out.print("Enter a string: ");
        String userInput = sc.nextLine();
        System.out.println("Minimum deletions: " + minDeletions(userInput));
    }
}
