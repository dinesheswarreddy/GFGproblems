//Smallest Divisor

import java.util.*;

class Solution {
    // Main logic to find the smallest divisor
    int smallestDivisor(int[] arr, int k) {
        int left = 1;
        int right = getMax(arr);
        int result = right;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int sum = getSum(arr, mid);

            if (sum <= k) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return result;
    }

    // Get maximum element in array
    private int getMax(int[] arr) {
        int max = arr[0];
        for (int val : arr) {
            max = Math.max(max, val);
        }
        return max;
    }

    // Get sum of ceiling values using math trick
    private int getSum(int[] arr, int divisor) {
        int sum = 0;
        for (int val : arr) {
            sum += (val + divisor - 1) / divisor;
        }
        return sum;
    }

    // Main function: takes input from user and also shows example
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution sol = new Solution();

        // User Input
        System.out.print("Enter size of array: ");
        int n = scanner.nextInt();
        int[] userArr = new int[n];
        System.out.println("Enter elements of array:");
        for (int i = 0; i < n; i++) {
            userArr[i] = scanner.nextInt();
        }
        System.out.print("Enter value of k: ");
        int userK = scanner.nextInt();

        int userResult = sol.smallestDivisor(userArr, userK);
        System.out.println("Smallest Divisor (User Input): " + userResult);

        // Built-in Example 1
        int[] exampleArr1 = {1, 2, 5, 9};
        int exampleK1 = 6;
        System.out.println("Built-in Example 1: Smallest Divisor = " +
            sol.smallestDivisor(exampleArr1, exampleK1));  // Output: 5

        // Built-in Example 2
        int[] exampleArr2 = {1, 1, 1, 1};
        int exampleK2 = 4;
        System.out.println("Built-in Example 2: Smallest Divisor = " +
            sol.smallestDivisor(exampleArr2, exampleK2));  // Output: 1
    }
}
