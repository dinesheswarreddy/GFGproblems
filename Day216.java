//All Palindromic Partitions

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // User input
        System.out.print("Enter a string: ");
        String s = sc.nextLine();

        Solution sol = new Solution();
        ArrayList<ArrayList<String>> result = sol.palinParts(s);

        // Print results
        System.out.println("All palindromic partitions:");
        for (ArrayList<String> partition : result) {
            System.out.println(partition);
        }
    }
}

// Optimized Solution Class
class Solution {
    public ArrayList<ArrayList<String>> palinParts(String s) {
        int n = s.length();
        ArrayList<ArrayList<String>> result = new ArrayList<>();

        // Precompute palindrome DP table
        boolean[][] dp = new boolean[n][n];
        for (int end = 0; end < n; end++) {
            for (int start = 0; start <= end; start++) {
                if (s.charAt(start) == s.charAt(end) &&
                    (end - start <= 2 || dp[start + 1][end - 1])) {
                    dp[start][end] = true;
                }
            }
        }

        // Backtrack using DP table
        backtrack(s, 0, new ArrayList<>(), result, dp);
        return result;
    }

    private void backtrack(String s, int start, ArrayList<String> currentList,
                           ArrayList<ArrayList<String>> result, boolean[][] dp) {
        if (start == s.length()) {
            result.add(new ArrayList<>(currentList));
            return;
        }

        for (int end = start; end < s.length(); end++) {
            if (dp[start][end]) {
                currentList.add(s.substring(start, end + 1));
                backtrack(s, end + 1, currentList, result, dp);
                currentList.remove(currentList.size() - 1); // backtrack
            }
        }
    }
}
