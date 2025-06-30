//Max min Height

import java.util.*;

class Solution {

    public int maxMinHeight(int[] arr, int k, int w) {
        int n = arr.length;
        int low = Integer.MAX_VALUE;
        int high = Integer.MIN_VALUE;

        for (int a : arr) {
            low = Math.min(low, a);
            high = Math.max(high, a);
        }

        high += k;

        int answer = low;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (isPossible(arr, k, w, mid)) {
                answer = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return answer;
    }

    private boolean isPossible(int[] arr, int k, int w, int target) {
        int n = arr.length;
        int[] added = new int[n + 1];
        long totalOps = 0;
        long currAdd = 0;

        for (int i = 0; i < n; i++) {
            currAdd += added[i];
            long currHeight = arr[i] + currAdd;

            if (currHeight < target) {
                long need = target - currHeight;
                totalOps += need;

                if (totalOps > k) return false;

                currAdd += need;
                if (i + w < added.length) {
                    added[i + w] -= need;
                }
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Enter number of flowers (n): ");
        String input = sc.nextLine().trim();
        
        if (input.isEmpty()) {
            // Built-in example
            int[] arr = {2, 3, 4, 5, 1};
            int k = 2;
            int w = 2;
            System.out.println("Using built-in example: arr = [2, 3, 4, 5, 1], k = 2, w = 2");
            int result = sol.maxMinHeight(arr, k, w);
            System.out.println("Max possible minimum height: " + result);
        } else {
            int n = Integer.parseInt(input);
            int[] arr = new int[n];

            System.out.println("Enter flower heights separated by space:");
            String[] arrStr = sc.nextLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(arrStr[i]);
            }

            System.out.println("Enter number of days (k):");
            int k = sc.nextInt();

            System.out.println("Enter width of watering (w):");
            int w = sc.nextInt();

            int result = sol.maxMinHeight(arr, k, w);
            System.out.println("Max possible minimum height: " + result);
        }

        sc.close();
    }
}
