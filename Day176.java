//Largest number in K swaps

import java.util.Scanner;

class Solution {
    private String max;

    // Function to find the largest number after k swaps.
    public String findMaximumNum(String s, int k) {
        max = s;
        char[] ch = s.toCharArray();
        helper(ch, k, 0);
        return max;
    }

    private void helper(char[] ch, int k, int index) {
        if (k <= 0 || index >= ch.length) {
            return;
        }

        char maxDigit = ch[index];
        for (int i = index + 1; i < ch.length; i++) {
            if (ch[i] > maxDigit) {
                maxDigit = ch[i];
            }
        }

        if (maxDigit != ch[index]) {
            k--;
        }

        for (int i = ch.length - 1; i >= index; i--) {
            if (ch[i] == maxDigit) {
                swap(ch, i, index);
                String s = new String(ch);
                if (s.compareTo(max) > 0) {
                    max = s;
                }
                helper(ch, k, index + 1);
                swap(ch, i, index); // backtrack
            }
        }
    }

    private void swap(char[] ch, int i, int j) {
        char temp = ch[i];
        ch[i] = ch[j];
        ch[j] = temp;
    }

    // Example usage
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Built-in example
        String example = "1034";
        int exampleK = 2;
        System.out.println("Built-in Test:");
        System.out.println("Input: " + example + ", k = " + exampleK);
        System.out.println("Output: " + solution.findMaximumNum(example, exampleK));

        // Input from user
        Scanner scanner = new Scanner(System.in);
        System.out.println("\nUser Input Test:");
        System.out.print("Enter the number string: ");
        String s = scanner.next();
        System.out.print("Enter number of swaps (k): ");
        int k = scanner.nextInt();
        String result = solution.findMaximumNum(s, k);
        System.out.println("Largest number after " + k + " swaps: " + result);
    }
}
