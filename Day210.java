//K closest elements
import java.util.*;

class Solution {

    int[] printKClosest(int[] arr, int k, int x) {
        // Max-heap to keep track of k closest elements
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (b[0] != a[0])
                return b[0] - a[0]; // Sort by distance descending
            return a[1] - b[1];     // If distances equal, keep larger element
        });

        for (int val : arr) {
            if (val == x) continue; // Skip x itself
            int dist = Math.abs(val - x);
            pq.offer(new int[]{dist, val});
            if (pq.size() > k) pq.poll(); // Keep only k closest
        }

        List<Integer> res = new ArrayList<>();
        while (!pq.isEmpty()) {
            res.add(pq.poll()[1]);
        }

        // Sort result based on rules
        res.sort((a, b) -> {
            int da = Math.abs(a - x);
            int db = Math.abs(b - x);
            if (da != db) return da - db;
            return b - a; // Prefer larger element if equal distance
        });

        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = res.get(i);
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        // === User input ===
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter sorted unique elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.print("Enter k: ");
        int k = sc.nextInt();

        System.out.print("Enter x (target): ");
        int x = sc.nextInt();

        int[] result = sol.printKClosest(arr, k, x);
        System.out.print("K closest elements: ");
        for (int num : result) {
            System.out.print(num + " ");
        }

        // === Built-in example for quick test ===
        System.out.println("\n\n--- Built-in Test ---");
        int[] testArr = {12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56};
        int kTest = 4;
        int xTest = 35;
        int[] resTest = sol.printKClosest(testArr, kTest, xTest);
        System.out.print("Built-in Test Output: ");
        for (int num : resTest) {
            System.out.print(num + " ");
        }
    }
}
