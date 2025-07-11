//Trail of ones

import java.util.Scanner;

class Solution {
    public int countConsec(int n) {
        int[] a = new int[n + 1]; // Strings ending with '0'
        int[] b = new int[n + 1]; // Strings ending with '1'

        a[1] = 1; // "0"
        b[1] = 1; // "1"

        for (int i = 2; i <= n; i++) {
            a[i] = a[i - 1] + b[i - 1];
            b[i] = a[i - 1];
        }

        int total = (int)Math.pow(2, n);
        int valid = a[n] + b[n];

        return total - valid;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt for input
        System.out.print("Enter the length of binary strings (n): ");
        int n = scanner.nextInt();

        // Create Solution object and get result
        Solution solution = new Solution();
        int result = solution.countConsec(n);

        // Print the result
        System.out.println("Number of binary strings of length " + n +
                           " with at least one pair of consecutive 1's: " + result);

        scanner.close();
    }
}
