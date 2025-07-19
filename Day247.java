//Count Unique Vowel Strings

import java.util.*;

public class Solution {

    public int vowelCount(String s) {
        Map<Character, List<Integer>> vowelMap = new HashMap<>();
        Set<Character> vowelsSet = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

        // Collect vowel positions
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (vowelsSet.contains(c)) {
                vowelMap.computeIfAbsent(c, k -> new ArrayList<>()).add(i);
            }
        }

        // Get the list of vowels present in the string
        List<Character> uniqueVowels = new ArrayList<>(vowelMap.keySet());
        int k = uniqueVowels.size();
        if (k == 0) return 0;

        // Compute product of the counts (combinations of picking one occurrence per vowel)
        int combinations = 1;
        for (char vowel : uniqueVowels) {
            combinations *= vowelMap.get(vowel).size();
        }

        // Multiply by k! for all permutations of the selected vowels
        int permutations = factorial(k);

        return combinations * permutations;
    }

    private int factorial(int n) {
        int result = 1;
        for (int i = 2; i <= n; i++) result *= i;
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);

        // User input
        System.out.print("Enter a lowercase string: ");
        String userInput = sc.nextLine().toLowerCase();
        int result = sol.vowelCount(userInput);
        System.out.println("Output: " + result);

        // Inbuilt test cases
        String[] testCases = {"aeiou", "ae", "aacidf", "xyz", "aaeeii"};
        System.out.println("\nRunning inbuilt test cases:");
        for (String test : testCases) {
            int res = sol.vowelCount(test);
            System.out.println("Input: \"" + test + "\" → Output: " + res);
        }

        sc.close();
    }
}
