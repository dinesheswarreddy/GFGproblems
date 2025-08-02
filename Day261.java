//Longest Subarray with Majority Greater than K
import java.util.*;

public class LongestSubarrayGreaterThanK {

    // Main logic method
    public static int longestSubarray(int[] arr, int k) {
        Map<Integer, Integer> firstOccurrence = new HashMap<>();
        int prefixSum = 0;
        int maxLength = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > k) {
                prefixSum += 1;
            } else {
                prefixSum -= 1;
            }

            if (prefixSum > 0) {
                maxLength = i + 1;
            } else {
                if (!firstOccurrence.containsKey(prefixSum)) {
                    firstOccurrence.put(prefixSum, i);
                }

                if (firstOccurrence.containsKey(prefixSum - 1)) {
                    int prevIndex = firstOccurrence.get(prefixSum - 1);
                    maxLength = Math.max(maxLength, i - prevIndex);
                }
            }
        }

        return maxLength;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Choose input type:");
        System.out.println("1. Use example input");
        System.out.println("2. Enter your own input");
        int choice = scanner.nextInt();

        int[] arr;
        int k;

        if (choice == 1) {
            // Example input
            arr = new int[]{1, 2, 3, 4, 1};
            k = 2;
            System.out.println("Using built-in input: arr = [1, 2, 3, 4, 1], k = 2");
        } else {
            // Custom input
            System.out.print("Enter size of array: ");
            int n = scanner.nextInt();
            arr = new int[n];
            System.out.println("Enter array elements:");
            for (int i = 0; i < n; i++) {
                arr[i] = scanner.nextInt();
            }
            System.out.print("Enter value of k: ");
            k = scanner.nextInt();
        }

        int result = longestSubarray(arr, k);
        System.out.println("Length of longest subarray: " + result);
    }
}
