//Longest Span in two Binary Arrays

import java.util.Scanner;
import java.util.HashMap;

class Solution {
    public int longestCommonSum(int[] a1, int[] a2) {
        int n = a1.length;
        int[] diff = new int[n];
        
        for (int i = 0; i < n; i++) {
            diff[i] = a1[i] - a2[i];
        }

        HashMap<Integer, Integer> map = new HashMap<>();
        int maxLen = 0;
        int prefixSum = 0;

        for (int i = 0; i < n; i++) {
            prefixSum += diff[i];

            if (prefixSum == 0) {
                maxLen = i + 1;
            }

            if (map.containsKey(prefixSum)) {
                maxLen = Math.max(maxLen, i - map.get(prefixSum));
            } else {
                map.put(prefixSum, i);
            }
        }

        return maxLen;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Take input size
        System.out.print("Enter size of the binary arrays: ");
        int n = sc.nextInt();

        int[] a1 = new int[n];
        int[] a2 = new int[n];

        // Input first array
        System.out.println("Enter elements of first binary array (0 or 1):");
        for (int i = 0; i < n; i++) {
            a1[i] = sc.nextInt();
        }

        // Input second array
        System.out.println("Enter elements of second binary array (0 or 1):");
        for (int i = 0; i < n; i++) {
            a2[i] = sc.nextInt();
        }

        // Call solution
        Solution sol = new Solution();
        int result = sol.longestCommonSum(a1, a2);
        System.out.println("Length of longest common span with same sum: " + result);
    }
}
