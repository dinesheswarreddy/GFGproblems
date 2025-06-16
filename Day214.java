//Equalize the Towers

import java.util.*;

class Solution {
    public int minCost(int[] heights, int[] cost) {
        int low = Integer.MAX_VALUE;
        int high = Integer.MIN_VALUE;

        for (int h : heights) {
            low = Math.min(low, h);
            high = Math.max(high, h);
        }

        int result = Integer.MAX_VALUE;
        while (low <= high) {
            int mid1 = low + (high - low) / 3;
            int mid2 = high - (high - low) / 3;

            int cost1 = getCost(heights, cost, mid1);
            int cost2 = getCost(heights, cost, mid2);

            result = Math.min(result, Math.min(cost1, cost2));

            if (cost1 < cost2) {
                high = mid2 - 1;
            } else {
                low = mid1 + 1;
            }
        }

        return result;
    }

    private int getCost(int[] heights, int[] cost, int targetHeight) {
        int totalCost = 0;
        for (int i = 0; i < heights.length; i++) {
            totalCost += Math.abs(heights[i] - targetHeight) * cost[i];
        }
        return totalCost;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Enter number of towers (or 0 to use example): ");
        int n = scanner.nextInt();

        int[] heights;
        int[] cost;

        if (n == 0) {
            // Built-in example
            heights = new int[]{1, 2, 3};
            cost = new int[]{10, 100, 1000};
            System.out.println("Using built-in example:");
            System.out.println("Heights: " + Arrays.toString(heights));
            System.out.println("Cost:    " + Arrays.toString(cost));
        } else {
            heights = new int[n];
            cost = new int[n];

            System.out.println("Enter heights:");
            for (int i = 0; i < n; i++) {
                heights[i] = scanner.nextInt();
            }

            System.out.println("Enter cost:");
            for (int i = 0; i < n; i++) {
                cost[i] = scanner.nextInt();
            }
        }

        int result = sol.minCost(heights, cost);
        System.out.println("Minimum cost to equalize all towers: " + result);
    }
}
