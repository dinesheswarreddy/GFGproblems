//Kth Smallest Number in Multiplication Table

import java.util.Scanner;

class Solution {

    public int kthSmallest(int m, int n, int k) {
        int low = 1, high = m * n;

        while (low < high) {
            int mid = low + (high - low) / 2;
            if (countLessEqual(mid, m, n) < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        return low;
    }

    // Helper function to count numbers <= x in the table
    private int countLessEqual(int x, int m, int n) {
        int count = 0;
        for (int i = 1; i <= m; i++) {
            count += Math.min(x / i, n);
        }
        return count;
    }

    // Main method with example usage
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example usage (inbuilt examples)
        System.out.println("Inbuilt Example 1: " + solution.kthSmallest(3, 3, 5)); // Output: 3
        System.out.println("Inbuilt Example 2: " + solution.kthSmallest(2, 3, 6)); // Output: 6

        // Example usage with user input
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter m (rows): ");
        int m = sc.nextInt();
        System.out.print("Enter n (columns): ");
        int n = sc.nextInt();
        System.out.print("Enter k (kth smallest): ");
        int k = sc.nextInt();

        int result = solution.kthSmallest(m, n, k);
        System.out.println("Kth smallest number in multiplication table: " + result);

        sc.close();
    }
}
