//Group Balls by Sequence

import java.util.*;

public class Solution {
    public boolean validgroup(int[] arr, int k) {
        if (arr.length % k != 0) return false;  // Can't divide into equal groups

        TreeMap<Integer, Integer> freqMap = new TreeMap<>();

        // Step 1: Build frequency map
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Step 2: Try forming groups
        while (!freqMap.isEmpty()) {
            int first = freqMap.firstKey(); // Get the smallest number
            int count = freqMap.get(first); // Number of groups we need to form

            for (int i = 0; i < k; i++) {
                int curr = first + i;
                if (!freqMap.containsKey(curr)) return false;

                int updatedCount = freqMap.get(curr) - count;
                if (updatedCount < 0) return false;
                else if (updatedCount == 0) freqMap.remove(curr);
                else freqMap.put(curr, updatedCount);
            }
        }

        return true;
    }

    // Main function to demonstrate user input and test cases
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution sol = new Solution();

        // ----------- User Input Example ----------
        System.out.println("Enter the number of balls:");
        int n = scanner.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter the numbers on the balls:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        System.out.println("Enter group size (k):");
        int k = scanner.nextInt();

        boolean result = sol.validgroup(arr, k);
        System.out.println("Can group into sequences? " + result);

        // ----------- Inbuilt Test Cases ----------
        System.out.println("\nRunning built-in test cases:");

        int[] test1 = {10, 1, 2, 11};
        int k1 = 2;
        System.out.println("Test 1: " + Arrays.toString(test1) + ", k = " + k1);
        System.out.println("Result: " + sol.validgroup(test1, k1)); // true

        int[] test2 = {7, 8, 9, 10, 11};
        int k2 = 2;
        System.out.println("Test 2: " + Arrays.toString(test2) + ", k = " + k2);
        System.out.println("Result: " + sol.validgroup(test2, k2)); // false

        scanner.close();
    }
}
