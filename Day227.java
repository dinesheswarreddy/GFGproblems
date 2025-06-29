//Split Array Largest Sum
import java.util.Scanner;

class Solution {
    public int splitArray(int[] arr, int k) {
        int low = 0, high = 0;
        for (int num : arr) {
            low = Math.max(low, num); // minimum possible max sum
            high += num;              // maximum possible max sum
        }

        while (low < high) {
            int mid = low + (high - low) / 2;
            if (canSplit(arr, k, mid)) {
                high = mid; // try smaller max sum
            } else {
                low = mid + 1; // need larger max sum
            }
        }

        return low;
    }

    private boolean canSplit(int[] arr, int k, int maxSumAllowed) {
        int currentSum = 0, splitsRequired = 1;
        for (int num : arr) {
            if (currentSum + num > maxSumAllowed) {
                splitsRequired++;
                currentSum = num;
                if (splitsRequired > k) return false;
            } else {
                currentSum += num;
            }
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Taking array size
        System.out.print("Enter size of array: ");
        int n = sc.nextInt();

        // Taking array elements
        int[] arr = new int[n];
        System.out.print("Enter " + n + " elements of array: ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Taking value of k
        System.out.print("Enter value of k (number of subarrays): ");
        int k = sc.nextInt();

        // Solve
        Solution solution = new Solution();
        int result = solution.splitArray(arr, k);

        // Output result
        System.out.println("Minimum possible maximum subarray sum: " + result);
    }
}
