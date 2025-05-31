//Kth element in Matrix

import java.util.*;

class Solution {
    // Function to find kth smallest element in a sorted matrix
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int low = matrix[0][0];
        int high = matrix[n - 1][n - 1];

        while (low < high) {
            int mid = low + (high - low) / 2;
            int count = countLessEqual(matrix, mid, n);

            if (count < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        return low;
    }

    // Helper to count elements ≤ val
    private int countLessEqual(int[][] matrix, int val, int n) {
        int count = 0;
        int row = n - 1, col = 0;

        while (row >= 0 && col < n) {
            if (matrix[row][col] <= val) {
                count += (row + 1);
                col++;
            } else {
                row--;
            }
        }

        return count;
    }

    // Main method to test with user input and built-in example
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Choose input mode:");
        System.out.println("1. Built-in example");
        System.out.println("2. User input");
        int choice = sc.nextInt();

        int[][] matrix;
        int k;

        if (choice == 1) {
            matrix = new int[][] {
                {10, 20, 30, 40},
                {15, 25, 35, 45},
                {24, 29, 37, 48},
                {32, 33, 39, 50}
            };
            k = 7;
            System.out.println("Built-in example:");
            System.out.println("Matrix: ");
            for (int[] row : matrix) {
                System.out.println(Arrays.toString(row));
            }
            System.out.println("k = " + k);
        } else {
            System.out.print("Enter matrix size n: ");
            int n = sc.nextInt();
            matrix = new int[n][n];
            System.out.println("Enter the matrix row by row:");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = sc.nextInt();
                }
            }
            System.out.print("Enter value of k: ");
            k = sc.nextInt();
        }

        int result = sol.kthSmallest(matrix, k);
        System.out.println("The " + k + "th smallest element is: " + result);
    }
}
