//Cutting Binary String

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution sol = new Solution();

        // User Input
        System.out.print("Enter a binary string: ");
        String userInput = scanner.nextLine();
        int result = sol.cuts(userInput);
        System.out.println("Minimum cuts for input \"" + userInput + "\": " + result);

        // Inbuilt test cases
        String[] testCases = {"101101101", "1111101", "00000", "1101", "101"};
        System.out.println("\n--- Inbuilt Test Cases ---");
        for (String s : testCases) {
            System.out.println("Input: " + s + " -> Output: " + sol.cuts(s));
        }

        scanner.close();
    }
}

class Solution {
    public int cuts(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -2); // -2 means uncomputed, -1 means impossible

        return dfs(s, 0, dp);
    }

    private int dfs(String s, int start, int[] dp) {
        if (start == s.length()) return 0;
        if (dp[start] != -2) return dp[start];

        int minCuts = Integer.MAX_VALUE;

        for (int end = start + 1; end <= s.length(); end++) {
            String substr = s.substring(start, end);
            if (isPowerOf5(substr)) {
                int result = dfs(s, end, dp);
                if (result != -1) {
                    minCuts = Math.min(minCuts, 1 + result);
                }
            }
        }

        dp[start] = (minCuts == Integer.MAX_VALUE) ? -1 : minCuts;
        return dp[start];
    }

    private boolean isPowerOf5(String bin) {
        if (bin.charAt(0) == '0') return false;
        long num = Long.parseLong(bin, 2);
        if (num == 0) return false;

        while (num % 5 == 0) {
            num /= 5;
        }
        return num == 1;
    }
}
