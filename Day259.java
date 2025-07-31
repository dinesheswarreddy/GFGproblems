//Powerful Integer

import java.util.*;

public class PowerfulIntegerFinder {

    public static int powerfulInteger(int[][] intervals, int k) {
        TreeMap<Integer, Integer> map = new TreeMap<>();

        // Step 1: Mark +1 at start and -1 at end+1
        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];

            map.put(start, map.getOrDefault(start, 0) + 1);
            map.put(end + 1, map.getOrDefault(end + 1, 0) - 1);
        }

        int active = 0;
        int lastPoint = -1;
        int maxPowerful = -1;

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int point = entry.getKey();

            if (lastPoint != -1 && active >= k) {
                // We're in a powerful segment from [lastPoint, point - 1]
                maxPowerful = Math.max(maxPowerful, point - 1);
            }

            active += entry.getValue();
            lastPoint = point;
        }

        return maxPowerful;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Choose input mode: (1) Manual (2) Inbuilt Sample");
        int mode = sc.nextInt();

        int[][] intervals;
        int k;

        if (mode == 1) {
            // Manual Input
            System.out.println("Enter number of intervals:");
            int n = sc.nextInt();
            intervals = new int[n][2];

            System.out.println("Enter intervals (start and end):");
            for (int i = 0; i < n; i++) {
                intervals[i][0] = sc.nextInt();
                intervals[i][1] = sc.nextInt();
            }

            System.out.println("Enter value of k:");
            k = sc.nextInt();
        } else {
            // Inbuilt Input Example
            System.out.println("Running with sample test case:");
            intervals = new int[][] {
                {1, 3},
                {4, 6},
                {3, 4}
            };
            k = 2;
        }

        int result = powerfulInteger(intervals, k);
        System.out.println("Maximum Powerful Integer = " + result);
    }
}
