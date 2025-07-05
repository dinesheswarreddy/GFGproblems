//Max Score from Subarray Mins

import java.util.*;

class Solution {
    // Function to compute max sum of smallest two in adjacent pairs
    public int maxSum(int[] arr) {
        int maxSum = 0;
        for (int i = 0; i < arr.length - 1; i++) {
            int sum = arr[i] + arr[i + 1];
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution solution = new Solution();

        // === Inbuilt Example ===
        int[] inbuiltArr = {4, 3, 5, 1};
        int resultInbuilt = solution.maxSum(inbuiltArr);
        System.out.println("Inbuilt example [4, 3, 5, 1] → Max Score: " + resultInbuilt);

        // === User Input ===
        System.out.print("Enter size of array: ");
        int n = scanner.nextInt();

        if (n < 2) {
            System.out.println("Array size must be at least 2.");
            return;
        }

        int[] userArr = new int[n];
        System.out.print("Enter " + n + " array elements: ");
        for (int i = 0; i < n; i++) {
            userArr[i] = scanner.nextInt();
        }

        int resultUser = solution.maxSum(userArr);
        System.out.println("User input → Max Score: " + resultUser);
    }
}
