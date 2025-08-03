//2D Difference Array

import java.util.*;

class Solution {
    public ArrayList<ArrayList<Integer>> applyDiff2D(int[][] mat, int[][] opr) {
        int n = mat.length;
        int m = mat[0].length;

        int[][] diff = new int[n + 2][m + 2];

        for (int[] op : opr) {
            int v = op[0];
            int r1 = op[1], c1 = op[2], r2 = op[3], c2 = op[4];

            diff[r1][c1] += v;
            diff[r1][c2 + 1] -= v;
            diff[r2 + 1][c1] -= v;
            diff[r2 + 1][c2 + 1] += v;
        }

        // Row-wise prefix sum
        for (int i = 0; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                diff[i][j] += diff[i][j - 1];
            }
        }

        // Column-wise prefix sum
        for (int j = 0; j <= m; j++) {
            for (int i = 1; i <= n; i++) {
                diff[i][j] += diff[i - 1][j];
            }
        }

        // Create result matrix
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 0; j < m; j++) {
                row.add(mat[i][j] + diff[i][j]);
            }
            result.add(row);
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Choose input type:\n1. User input\n2. Inbuilt example");
        int choice = sc.nextInt();

        int[][] mat, opr;
        if (choice == 1) {
            // User Input
            System.out.print("Enter number of rows and columns (n m): ");
            int n = sc.nextInt();
            int m = sc.nextInt();
            mat = new int[n][m];

            System.out.println("Enter matrix elements row-wise:");
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    mat[i][j] = sc.nextInt();

            System.out.print("Enter number of operations (q): ");
            int q = sc.nextInt();
            opr = new int[q][5];

            System.out.println("Enter each operation in format: v r1 c1 r2 c2");
            for (int i = 0; i < q; i++)
                for (int j = 0; j < 5; j++)
                    opr[i][j] = sc.nextInt();

        } else {
            // Inbuilt Example
            mat = new int[][]{
                {1, 2, 3},
                {1, 1, 0},
                {4, -2, 2}
            };

            opr = new int[][]{
                {2, 0, 0, 1, 1},
                {-1, 1, 0, 2, 2}
            };
        }

        ArrayList<ArrayList<Integer>> finalMatrix = sol.applyDiff2D(mat, opr);

        System.out.println("\nFinal Matrix:");
        for (ArrayList<Integer> row : finalMatrix) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }

        sc.close();
    }
}
