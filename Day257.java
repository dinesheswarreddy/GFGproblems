//ASCII Range Sum
import java.util.*;

class Solution {
    public ArrayList<Integer> asciirange(String s) {
        ArrayList<Integer> result = new ArrayList<>();
        int n = s.length();
        Map<Character, Integer> firstIndex = new HashMap<>();

        // Step 1: Record first occurrence of each character
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (!firstIndex.containsKey(ch)) {
                firstIndex.put(ch, i);
            }
        }

        // Step 2: Check last occurrence and calculate ASCII sums
        for (char ch = 'a'; ch <= 'z'; ch++) {
            if (firstIndex.containsKey(ch)) {
                int first = firstIndex.get(ch);
                int last = s.lastIndexOf(ch);

                if (first != last && last - first > 1) {
                    int sum = 0;
                    for (int i = first + 1; i < last; i++) {
                        sum += (int) s.charAt(i);
                    }
                    result.add(sum);
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Take input from user
        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        Solution solution = new Solution();
        ArrayList<Integer> output = solution.asciirange(input);

        // Print result
        System.out.println("ASCII Range Sums: " + output);
    }
}
