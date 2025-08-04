//Maximum sum Rectangle

import java.util.Scanner;

class Solution {
    public int maxRectSum(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        int maxSum = Integer.MIN_VALUE;

        for (int top = 0; top < n; top++) {
            int[] temp = new int[m];

            for (int bottom = top; bottom < n; bottom++) {
                for (int col = 0; col < m; col++) {
                    temp[col] += mat[bottom][col];
                }

                int currMax = kadane(temp);
                maxSum = Math.max(maxSum, currMax);
            }
        }

        return maxSum;
    }

    private int kadane(int[] arr) {
        int maxSoFar = arr[0];
        int maxEndingHere = arr[0];

        for (int i = 1; i < arr.length; i++) {
            maxEndingHere = Math.max(arr[i], maxEndingHere + arr[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }

        return maxSoFar;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Choose input type:");
        System.out.println("1. Use built-in test case");
        System.out.println("2. Enter custom matrix");
        int choice = sc.nextInt();

        int[][] mat;

        if (choice == 1) {
            mat = new int[][] {
                {1, 2, -1, -4, -20},
                {-8, -3, 4, 2, 1},
                {3, 8, 10, 1, 3},
                {-4, -1, 1, 7, -6}
            };
        } else {
            System.out.print("Enter number of rows (n): ");
            int n = sc.nextInt();
            System.out.print("Enter number of columns (m): ");
            int m = sc.nextInt();

            mat = new int[n][m];

            System.out.println("Enter matrix elements row by row:");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    mat[i][j] = sc.nextInt();
                }
            }
        }

        Solution sol = new Solution();
        int result = sol.maxRectSum(mat);

        System.out.println("Maximum sum rectangle = " + result);
    }
}
