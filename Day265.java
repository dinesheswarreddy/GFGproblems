//Roman Number to Integer
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Solution {
    // Method to convert Roman numeral to integer
    public int romanToDecimal(String s) {
        // Roman to integer mapping
        Map<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);

        int total = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int currVal = romanMap.get(s.charAt(i));
            if (i < n - 1 && currVal < romanMap.get(s.charAt(i + 1))) {
                total -= currVal;
            } else {
                total += currVal;
            }
        }

        return total;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution solution = new Solution();

        // Take input from user
        System.out.print("Enter Roman numeral (e.g., IX, XL, MCMIV): ");
        String roman = scanner.nextLine().toUpperCase();  // Convert to uppercase for safety

        // Convert and print result
        int result = solution.romanToDecimal(roman);
        System.out.println("Integer value: " + result);

        // Optional: some built-in test cases
        System.out.println("\n--- Sample Test Cases ---");
        System.out.println("IX -> " + solution.romanToDecimal("IX"));       // 9
        System.out.println("XL -> " + solution.romanToDecimal("XL"));       // 40
        System.out.println("MCMIV -> " + solution.romanToDecimal("MCMIV")); // 1904
    }
}
