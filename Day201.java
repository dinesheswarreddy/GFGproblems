//Substrings with K Distinct
import java.util.HashMap;
import java.util.Scanner;

class Solution {
    public int countSubstr(String s, int k) {
        return atMostKDistinct(s, k) - atMostKDistinct(s, k - 1);
    }

    private int atMostKDistinct(String s, int k) {
        if (k == 0) return 0;

        int left = 0, result = 0;
        HashMap<Character, Integer> map = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            map.put(ch, map.getOrDefault(ch, 0) + 1);

            while (map.size() > k) {
                char leftChar = s.charAt(left);
                map.put(leftChar, map.get(leftChar) - 1);
                if (map.get(leftChar) == 0) {
                    map.remove(leftChar);
                }
                left++;
            }

            result += right - left + 1;
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner sc = new Scanner(System.in);

        // 🔹 User Input
        System.out.print("Enter the string: ");
        String inputStr = sc.nextLine();

        System.out.print("Enter the value of k: ");
        int k = sc.nextInt();

        int result = solution.countSubstr(inputStr, k);
        System.out.println("Count of substrings with exactly " + k + " distinct characters: " + result);

        // 🔹 Inbuilt Example
        System.out.println("\n--- Inbuilt Test Cases ---");
        System.out.println("Input: s = \"abc\", k = 2 → Output: " + solution.countSubstr("abc", 2));
        System.out.println("Input: s = \"aba\", k = 2 → Output: " + solution.countSubstr("aba", 2));
        System.out.println("Input: s = \"aa\",  k = 1 → Output: " + solution.countSubstr("aa", 1));
    }
}
