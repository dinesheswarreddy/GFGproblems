//Balancing Consonants and Vowels Ratio

import java.util.Scanner;

public class Solution {
    public int countBalanced(String[] arr) {
        int n = arr.length;
        
        java.util.Set<Character> vowels = new java.util.HashSet<>();
        vowels.add('a'); vowels.add('e'); vowels.add('i'); vowels.add('o'); vowels.add('u');
        
        int[] diff = new int[n];
        
        for (int i = 0; i < n; i++) {
            int vCount = 0, cCount = 0;
            for (char ch : arr[i].toCharArray()) {
                if (vowels.contains(ch)) vCount++;
                else cCount++;
            }
            diff[i] = vCount - cCount;
        }
        
        long[] prefixDiff = new long[n + 1];
        prefixDiff[0] = 0;
        for (int i = 1; i <= n; i++) {
            prefixDiff[i] = prefixDiff[i - 1] + diff[i - 1];
        }
        
        java.util.HashMap<Long, Integer> freq = new java.util.HashMap<>();
        int count = 0;
        
        for (long val : prefixDiff) {
            int c = freq.getOrDefault(val, 0);
            count += c;
            freq.put(val, c + 1);
        }
        
        return count;
    }

    // Main method to take input and run example
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter number of strings: ");
        int n = sc.nextInt();
        sc.nextLine();  // consume newline
        
        String[] arr = new String[n];
        System.out.println("Enter the strings:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLine();
        }
        
        Solution sol = new Solution();
        int result = sol.countBalanced(arr);
        System.out.println("Number of balanced subarrays: " + result);
        
        sc.close();
    }
}
