//Longest Substring with K Uniques

import java.util.*;

class Solution {
    public int longestKSubstr(String s, int k) {
        if (s == null || s.length() == 0 || k == 0) return -1;

        Map<Character, Integer> freqMap = new HashMap<>();
        int maxLength = -1;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);

            while (freqMap.size() > k) {
                char leftChar = s.charAt(left);
                freqMap.put(leftChar, freqMap.get(leftChar) - 1);
                if (freqMap.get(leftChar) == 0) {
                    freqMap.remove(leftChar);
                }
                left++;
            }

            if (freqMap.size() == k) {
                maxLength = Math.max(maxLength, right - left + 1);
            }
        }

        return maxLength;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution solution = new Solution();

        // Take input from user
        System.out.print("Enter the string: ");
        String inputString = scanner.nextLine();

        System.out.print("Enter value of k: ");
        int k = scanner.nextInt();

        int result = solution.longestKSubstr(inputString, k);
        System.out.println("Longest substring length with exactly " + k + " unique characters: " + result);

        // Inbuilt test examples
        System.out.println("\nRunning inbuilt test cases:");
        System.out.println("Input: \"aabacbebebe\", k = 3 → Output: " +
                solution.longestKSubstr("aabacbebebe", 3)); // Expected: 7
        System.out.println("Input: \"aaaa\", k = 2 → Output: " +
                solution.longestKSubstr("aaaa", 2)); // Expected: -1
        System.out.println("Input: \"aabaaab\", k = 2 → Output: " +
                solution.longestKSubstr("aabaaab", 2)); // Expected: 7
    }
}
