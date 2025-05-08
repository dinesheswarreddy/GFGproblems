//Missing element of Arthimetic Progression

import java.util.Scanner;

class Solution {
    public int findMissing(int[] arr) {
        int n = arr.length;
        int d = 0;

        if (n == 2) {
            d = arr[1] - arr[0];
        } else {
            if (arr[1] - arr[0] <= 0) {
                d = Math.max(arr[1] - arr[0], arr[2] - arr[1]);
            } else {
                d = Math.min(arr[1] - arr[0], arr[2] - arr[1]);
            }
        }

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i - 1] + d) {
                return arr[i - 1] + d;
            }
        }

        return arr[n - 1] + d;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Example 1: Hardcoded input
        int[] exampleArray = {2, 4, 6, 10}; // Missing 8
        System.out.println("Missing number in hardcoded array: " + sol.findMissing(exampleArray));

        // Example 2: User input
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements in the array: ");
        int n = sc.nextInt();

        int[] userArray = new int[n];
        System.out.println("Enter " + n + " elements of the arithmetic progression (with one missing):");
        for (int i = 0; i < n; i++) {
            userArray[i] = sc.nextInt();
        }

        int missing = sol.findMissing(userArray);
        System.out.println("Missing number in user-provided array: " + missing);

        sc.close();
    }
}
