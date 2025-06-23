//Minimum sum

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Take size of input
        System.out.print("Enter number of digits: ");
        int n = sc.nextInt();

        // Take array input
        int[] arr = new int[n];
        System.out.print("Enter the digits (0–9) separated by space: ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        String result = solution.minSum(arr);

        System.out.println("Minimum possible sum: " + result);
    }
}

// Solution class with logic
class Solution {
    String minSum(int[] arr) {
        Arrays.sort(arr);
        StringBuilder num1 = new StringBuilder();
        StringBuilder num2 = new StringBuilder();

        // Distribute digits alternately
        for (int i = 0; i < arr.length; i++) {
            if (i % 2 == 0)
                num1.append(arr[i]);
            else
                num2.append(arr[i]);
        }

        return stripLeadingZeros(addStrings(num1.toString(), num2.toString()));
    }

    private String addStrings(String num1, String num2) {
        StringBuilder result = new StringBuilder();
        int carry = 0, i = num1.length() - 1, j = num2.length() - 1;

        while (i >= 0 || j >= 0 || carry > 0) {
            int x = i >= 0 ? num1.charAt(i--) - '0' : 0;
            int y = j >= 0 ? num2.charAt(j--) - '0' : 0;
            int sum = x + y + carry;
            result.append(sum % 10);
            carry = sum / 10;
        }

        return result.reverse().toString();
    }

    private String stripLeadingZeros(String str) {
        int i = 0;
        while (i < str.length() - 1 && str.charAt(i) == '0') {
            i++;
        }
        return str.substring(i);
    }
}
