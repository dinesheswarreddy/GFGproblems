//Check if frequencies can be equal

import java.util.*;

public class Solution {
    
    static boolean sameFreq(String s) {
        Map<Character, Integer> charCount = new HashMap<>();
        
        // Count frequency of each character
        for (char ch : s.toCharArray()) {
            charCount.put(ch, charCount.getOrDefault(ch, 0) + 1);
        }

        // Count frequency of those frequencies
        Map<Integer, Integer> freqCount = new HashMap<>();
        for (int freq : charCount.values()) {
            freqCount.put(freq, freqCount.getOrDefault(freq, 0) + 1);
        }

        if (freqCount.size() == 1) return true;

        if (freqCount.size() == 2) {
            List<Integer> freqs = new ArrayList<>(freqCount.keySet());
            int freq1 = freqs.get(0), freq2 = freqs.get(1);
            int count1 = freqCount.get(freq1), count2 = freqCount.get(freq2);

            // Case 1: One frequency is 1 and occurs once
            if ((freq1 == 1 && count1 == 1) || (freq2 == 1 && count2 == 1)) {
                return true;
            }

            // Case 2: Frequencies differ by 1 and higher freq occurs once
            if ((Math.abs(freq1 - freq2) == 1) &&
                ((freq1 > freq2 && count1 == 1) || (freq2 > freq1 && count2 == 1))) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 🔹 Predefined Test Cases
        String[] testCases = {"xyyz", "xyyzz", "xxxxyyzz", "aabbccdde", "abc", "a"};
        System.out.println("🔍 Predefined Test Cases:");
        for (String test : testCases) {
            System.out.println("Input: " + test + " -> Output: " + sameFreq(test));
        }

        // 🔸 Custom User Input
        System.out.print("\nEnter your own string to test: ");
        String userInput = scanner.nextLine().toLowerCase();
        System.out.println("Result: " + sameFreq(userInput));
        
        scanner.close();
    }
}
