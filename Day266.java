//Difference Check

import java.util.*;

class Solution {
    public int minDifference(String[] arr) {
        int n = arr.length;
        int[] seconds = new int[n];

        // Convert each time to seconds
        for (int i = 0; i < n; i++) {
            String[] parts = arr[i].split(":");
            int h = Integer.parseInt(parts[0]);
            int m = Integer.parseInt(parts[1]);
            int s = Integer.parseInt(parts[2]);
            seconds[i] = h * 3600 + m * 60 + s;
        }

        // Sort the array of seconds
        Arrays.sort(seconds);

        // Initialize minDiff with max possible value
        int minDiff = Integer.MAX_VALUE;

        // Compare each pair of consecutive times
        for (int i = 1; i < n; i++) {
            minDiff = Math.min(minDiff, seconds[i] - seconds[i - 1]);
        }

        // Check circular difference (wrap around midnight)
        int circularDiff = 86400 - seconds[n - 1] + seconds[0];
        minDiff = Math.min(minDiff, circularDiff);

        return minDiff;
    }

    // Main function for testing and user input
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read number of elements
        System.out.print("Enter number of time strings: ");
        int n = sc.nextInt();
        sc.nextLine(); // Consume the newline character

        String[] arr = new String[n];

        // Read time strings
        System.out.println("Enter time strings in HH:MM:SS format:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLine();
        }

        // Create Solution object and call minDifference
        Solution sol = new Solution();
        int result = sol.minDifference(arr);

        // Output the result
        System.out.println("Minimum difference in seconds: " + result);

        sc.close();
    }
}
