//Count Numbers Containing Specific Digits
import java.util.*;

class Solution {
    public int countValid(int n, int[] arr) {
        // Step 1: Prepare a set of banned digits
        Set<Integer> banned = new HashSet<>();
        for (int d : arr) banned.add(d);
        
        // Step 2: Count allowed digits
        List<Integer> allowed = new ArrayList<>();
        for (int d = 0; d <= 9; d++) {
            if (!banned.contains(d)) allowed.add(d);
        }

        int total = 9 * (int)Math.pow(10, n - 1);

        // If no allowed digits, then all numbers are valid
        if (allowed.size() == 0) return total;

        // Step 3: Count invalid n-digit numbers (that use only allowed digits)
        int invalid = 0;
        for (int firstDigit : allowed) {
            if (firstDigit == 0) continue; // skip leading zero

            int count = 1;
            for (int i = 1; i < n; i++) {
                count *= allowed.size(); // all positions can use any allowed digit
            }
            invalid += count;
        }

        return total - invalid;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution sol = new Solution();

        // ✅ Example 1: Hardcoded test case
        int n1 = 2;
        int[] arr1 = {3, 5};
        System.out.println("Example 1 Output (n = 2, arr = [3, 5]): " + sol.countValid(n1, arr1));

        // ✅ Example 2: Take user input
        System.out.print("\nEnter value of n: ");
        int n = scanner.nextInt();

        System.out.print("Enter size of array: ");
        int size = scanner.nextInt();

        int[] arr = new int[size];
        System.out.print("Enter " + size + " digits (space-separated): ");
        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }

        int result = sol.countValid(n, arr);
        System.out.println("Count of valid " + n + "-digit numbers: " + result);

        scanner.close();
    }
}
