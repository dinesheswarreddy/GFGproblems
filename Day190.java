//Dice throw
import java.util.Scanner;

class Solution {
    static int noOfWays(int m, int n, int x) {
        int[][] dp = new int[n + 1][x + 1];

        dp[0][0] = 1;

        for (int dice = 1; dice <= n; dice++) {
            for (int sum = 1; sum <= x; sum++) {
                dp[dice][sum] = 0;
                for (int face = 1; face <= m; face++) {
                    if (sum - face >= 0) {
                        dp[dice][sum] += dp[dice - 1][sum - face];
                    }
                }
            }
        }

        return dp[n][x];
    }

    public static void main(String[] args) {
        // In-built example usage
        System.out.println("In-built Example:");
        int m1 = 6, n1 = 3, x1 = 12;
        System.out.println("Ways to get sum " + x1 + " with " + n1 + " dice of " + m1 + " faces: " + noOfWays(m1, n1, x1));
        
        // Taking input from user
        Scanner sc = new Scanner(System.in);
        System.out.println("\nEnter number of faces (m): ");
        int m = sc.nextInt();

        System.out.println("Enter number of dice (n): ");
        int n = sc.nextInt();

        System.out.println("Enter desired sum (x): ");
        int x = sc.nextInt();

        int ways = noOfWays(m, n, x);
        System.out.println("Ways to get sum " + x + " with " + n + " dice of " + m + " faces: " + ways);
    }
}
