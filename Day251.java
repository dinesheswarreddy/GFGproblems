//Sum of Subarrays

import java.util.Scanner;

class Solution {
    public int subarraySum(int[] arr) {
        int n = arr.length;
        int totalSum = 0;

        for (int i = 0; i < n; i++) {
            totalSum += arr[i] * (i + 1) * (n - i);
        }

        return totalSum;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Take input from user
        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter the elements of the array:");
        for(int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        // Create Solution object and compute result
        Solution solution = new Solution();
        int result = solution.subarraySum(arr);

        // Print result
        System.out.println("Sum of all subarrays: " + result);
    }
}
