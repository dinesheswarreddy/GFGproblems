//Find rectangle with corners as 1

import java.util.*;

class Solution {
    public boolean ValidCorner(int mat[][]) {
        int n = mat.length;
        int m = mat[0].length;

        Set<String> seenPairs = new HashSet<>();

        for (int i = 0; i < n; i++) {
            for (int c1 = 0; c1 < m; c1++) {
                if (mat[i][c1] == 1) {
                    for (int c2 = c1 + 1; c2 < m; c2++) {
                        if (mat[i][c2] == 1) {
                            String pair = c1 + "," + c2;
                            if (seenPairs.contains(pair)) {
                                return true; // Rectangle found
                            }
                            seenPairs.add(pair);
                        }
                    }
                }
            }
        }
        return false; // No rectangle found
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Choose input type:\n1. Manual Input\n2. Use Inbuilt Example");
        int choice = sc.nextInt();

        int[][] mat;

        if (choice == 1) {
            // Manual Input
            System.out.print("Enter number of rows: ");
            int n = sc.nextInt();
            System.out.print("Enter number of columns: ");
            int m = sc.nextInt();
            mat = new int[n][m];
            System.out.println("Enter matrix elements (only 0s and 1s):");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    mat[i][j] = sc.nextInt();
                }
            }
        } else {
            // Inbuilt Example
            mat = new int[][] {
                {1, 0, 0, 1, 0},
                {0, 0, 1, 0, 1},
                {0, 0, 0, 1, 0},
                {1, 0, 1, 0, 1}
            };
            System.out.println("Using inbuilt matrix:");
            for (int[] row : mat) {
                System.out.println(Arrays.toString(row));
            }
        }

        boolean result = sol.ValidCorner(mat);
        System.out.println("Output: " + result);
    }
}
