//Substrings of length k with k-1 distinct elements

import java.util.Scanner;

class Solution {
    public int substrCount(String s, int k) {
        if (s.length() < k) return 0;

        int[] freq = new int[26];
        int distinct = 0, count = 0;

        for (int i = 0; i < s.length(); i++) {
            // Add current character
            int idx = s.charAt(i) - 'a';
            if (freq[idx] == 0) distinct++;
            freq[idx]++;

            // Remove character if window > k
            if (i >= k) {
                int leftIdx = s.charAt(i - k) - 'a';
                freq[leftIdx]--;
                if (freq[leftIdx] == 0) distinct--;
            }

            // Check window of size k
            if (i >= k - 1 && distinct == k - 1) {
                count++;
            }
        }

        return count;
    }

    // Main method to take input from user and call substrCount
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Input string
        System.out.print("Enter the string: ");
        String s = sc.nextLine();
        
        // Input value of k
        System.out.print("Enter the value of k: ");
        int k = sc.nextInt();

        // Call the method
        Solution sol = new Solution();
        int result = sol.substrCount(s, k);

        // Output result
        System.out.println("Count of substrings of length " + k + " with " + (k - 1) + " distinct characters: " + result);
    }
}
