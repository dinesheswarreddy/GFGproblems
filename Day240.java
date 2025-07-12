//Gold Mine Problem
import java.util.*;

class Solution {
    public int maxGold(int[][] mat) {
        int n = mat.length;        // number of rows
        int m = mat[0].length;     // number of columns
        int[][] dp = new int[n][m];

        // Fill the last column
        for (int i = 0; i < n; i++) {
            dp[i][m - 1] = mat[i][m - 1];
        }

        // Fill rest of the dp table
        for (int j = m - 2; j >= 0; j--) {
            for (int i = 0; i < n; i++) {
                int right = dp[i][j + 1];
                int rightUp = (i > 0) ? dp[i - 1][j + 1] : 0;
                int rightDown = (i < n - 1) ? dp[i + 1][j + 1] : 0;

                dp[i][j] = mat[i][j] + Math.max(right, Math.max(rightUp, rightDown));
            }
        }

        // Get max from the first column
        int maxGold = 0;
        for (int i = 0; i < n; i++) {
            maxGold = Math.max(maxGold, dp[i][0]);
        }

        return maxGold;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Choose input method:");
        System.out.println("1. Manual input");
        System.out.println("2. Use built-in example");
        int choice = sc.nextInt();

        int[][] mat;

        if (choice == 1) {
            System.out.print("Enter number of rows: ");
            int n = sc.nextInt();
            System.out.print("Enter number of columns: ");
            int m = sc.nextInt();

            mat = new int[n][m];
            System.out.println("Enter the gold mine matrix:");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    mat[i][j] = sc.nextInt();
                }
            }
        } else {
            // Built-in test case
            mat = new int[][]{
                {1, 3, 1, 5},
                {2, 2, 4, 1},
                {5, 0, 2, 3},
                {0, 6, 1, 2}
            };
            System.out.println("Using built-in matrix:");
            for (int[] row : mat) {
                System.out.println(Arrays.toString(row));
            }
        }

        int result = sol.maxGold(mat);
        System.out.println("Maximum gold collected: " + result);
    }
}
