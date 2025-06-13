//Koko Eating Bananas

import java.util.Scanner;

class Solution {
    public int kokoEat(int[] arr, int k) {
        int left = 1;
        int right = 0;

        for (int bananas : arr) {
            right = Math.max(right, bananas);
        }

        int answer = right;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canFinish(arr, k, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return answer;
    }

    private boolean canFinish(int[] arr, int k, int s) {
        int hours = 0;
        for (int bananas : arr) {
            hours += (bananas + s - 1) / s; // equivalent to ceil(bananas / s)
        }
        return hours <= k;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input: size of array
        System.out.print("Enter number of piles: ");
        int n = sc.nextInt();

        // Input: elements of the array
        int[] arr = new int[n];
        System.out.print("Enter pile sizes: ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Input: number of hours
        System.out.print("Enter number of hours (k): ");
        int k = sc.nextInt();

        // Solve using Solution class
        Solution sol = new Solution();
        int minSpeed = sol.kokoEat(arr, k);

        // Output
        System.out.println("Minimum bananas per hour Koko needs to eat: " + minSpeed);
    }
}
