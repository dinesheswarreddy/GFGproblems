//Count pairs Sum in matrices

import java.util.HashSet;
import java.util.Scanner;

class Solution {
    // Method to count valid pairs
    int countPairs(int[][] mat1, int[][] mat2, int x) {
        int n = mat1.length;
        HashSet<Integer> set = new HashSet<>();

        // Add all elements of mat2 to the set
        for (int[] row : mat2) {
            for (int num : row) {
                set.add(num);
            }
        }

        int count = 0;

        // Traverse mat1 and check for complement
        for (int[] row : mat1) {
            for (int num : row) {
                if (set.contains(x - num)) {
                    count++;
                }
            }
        }

        return count;
    }
}

public class Tester {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        // ------------------ User Input ------------------
        System.out.print("Enter size of matrix (n): ");
        int n = sc.nextInt();

        int[][] mat1 = new int[n][n];
        int[][] mat2 = new int[n][n];

        System.out.println("Enter elements of mat1:");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                mat1[i][j] = sc.nextInt();

        System.out.println("Enter elements of mat2:");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                mat2[i][j] = sc.nextInt();

        System.out.print("Enter target sum x: ");
        int x = sc.nextInt();

        int userCount = sol.countPairs(mat1, mat2, x);
        System.out.println("Number of valid pairs (User Input): " + userCount);

        // ------------- Inbuilt Example (Hardcoded) -------------
        int[][] mat1Ex = {{1, 5, 6}, {8, 10, 11}, {15, 16, 18}};
        int[][] mat2Ex = {{2, 4, 7}, {9, 10, 12}, {13, 16, 20}};
        int xEx = 21;
        int builtInCount = sol.countPairs(mat1Ex, mat2Ex, xEx);

        System.out.println("\nExample from question:");
        System.out.println("Number of valid pairs (Example): " + builtInCount);
    }
}
