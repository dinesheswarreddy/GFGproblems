//Longest Prefix Suffix

import java.util.Scanner;

class Solution {
    int getLPSLength(String s) {
        int n = s.length();
        int[] lps = new int[n];

        int len = 0;
        int i = 1;

        while (i < n) {
            if (s.charAt(i) == s.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }

        return lps[n - 1];  // length of the longest proper prefix which is also suffix
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        int result = sol.getLPSLength(input);
        System.out.println("Length of longest proper prefix which is also suffix: " + result);

        // Sample usage:
        System.out.println("\nSample Test Cases:");
        System.out.println("Input: abab → Output: " + sol.getLPSLength("abab"));
        System.out.println("Input: aabcdaabc → Output: " + sol.getLPSLength("aabcdaabc"));
        System.out.println("Input: aaaa → Output: " + sol.getLPSLength("aaaa"));

        sc.close();
    }
}
