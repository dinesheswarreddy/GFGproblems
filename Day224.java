//Game with String

import java.util.*;

class Solution {
    public int minValue(String s, int k) {
        int[] freq = new int[26];
        
        // Step 1: Count frequencies
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }
        
        // Step 2: Max-heap to store frequencies
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int f : freq) {
            if (f > 0) {
                maxHeap.add(f);
            }
        }
        
        // Step 3: Remove k characters
        while (k > 0 && !maxHeap.isEmpty()) {
            int top = maxHeap.poll();
            top--;
            k--;
            if (top > 0) {
                maxHeap.add(top);
            }
        }
        
        // Step 4: Compute value
        int result = 0;
        while (!maxHeap.isEmpty()) {
            int f = maxHeap.poll();
            result += f * f;
        }
        
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        // User input
        System.out.print("Enter the string (lowercase letters only): ");
        String s = sc.nextLine();

        System.out.print("Enter the value of k: ");
        int k = sc.nextInt();

        // Call and print result
        int minValue = sol.minValue(s, k);
        System.out.println("Minimum value of string after removing " + k + " characters: " + minValue);
    }
}
