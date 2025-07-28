//Make Matrix Beautiful

import java.util.Scanner;

class Solution {
    // Core function to balance matrix and count operations
    public static int balanceSums(int[][] mat) {
        int n = mat.length;
        int[] rowSum = new int[n];
        int[] colSum = new int[n];

        // Step 1: Calculate row and column sums
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rowSum[i] += mat[i][j];
                colSum[j] += mat[i][j];
            }
        }

        // Step 2: Find the maximum row or column sum
        int maxSum = 0;
        for (int i = 0; i < n; i++) {
            maxSum = Math.max(maxSum, rowSum[i]);
            maxSum = Math.max(maxSum, colSum[i]);
        }

        // Step 3: Total number of operations = sum of (maxSum - each rowSum)
        int operations = 0;
        for (int i = 0; i < n; i++) {
            operations += (maxSum - rowSum[i]);
        }

        return operations;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // ---------- User Input ----------
        System.out.println("Enter size of the square matrix (n): ");
        int n = scanner.nextInt();

        int[][] userMat = new int[n][n];
        System.out.println("Enter matrix elements row-wise:");

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                userMat[i][j] = scanner.nextInt();
            }
        }

        int userResult = balanceSums(userMat);
        System.out.println("Minimum operations to make user matrix beautiful: " + userResult);

        // ---------- Inbuilt Example ----------
        int[][] inbuiltMat = {
            {1, 2, 3},
            {4, 2, 3},
            {3, 2, 1}
        };

        int inbuiltResult = balanceSums(inbuiltMat);
        System.out.println("Minimum operations for inbuilt matrix: " + inbuiltResult);
    }
}

