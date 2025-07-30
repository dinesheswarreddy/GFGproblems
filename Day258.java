//Subarrays with sum K

import java.util.HashMap;
import java.util.Scanner;

class Solution {
    // Method to count subarrays with sum k
    public int cntSubarrays(int[] arr, int k) {
        HashMap<Integer, Integer> prefixSumFreq = new HashMap<>();
        int currSum = 0;
        int count = 0;

        for (int num : arr) {
            currSum += num;

            if (currSum == k) {
                count++;
            }

            if (prefixSumFreq.containsKey(currSum - k)) {
                count += prefixSumFreq.get(currSum - k);
            }

            prefixSumFreq.put(currSum, prefixSumFreq.getOrDefault(currSum, 0) + 1);
        }

        return count;
    }

    // Main method
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution sol = new Solution();

        // ---- User Input Example ----
        System.out.print("Enter the size of array: ");
        int n = scanner.nextInt();

        int[] userArr = new int[n];
        System.out.print("Enter " + n + " elements: ");
        for (int i = 0; i < n; i++) {
            userArr[i] = scanner.nextInt();
        }

        System.out.print("Enter target sum k: ");
        int userK = scanner.nextInt();

        int userResult = sol.cntSubarrays(userArr, userK);
        System.out.println("User Input Result: " + userResult);

        // ---- Built-in Example ----
        int[] arr = {10, 2, -2, -20, 10};
        int k = -10;
        int result = sol.cntSubarrays(arr, k);
        System.out.println("Built-in Example Result (arr = [10, 2, -2, -20, 10], k = -10): " + result);

        scanner.close();
    }
}
