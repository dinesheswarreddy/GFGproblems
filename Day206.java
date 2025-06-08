//Sum-string

import java.util.Scanner;

class Solution {
    public boolean isSumString(String s) {
        int n = s.length();
        
        // Try all pairs for the first and second numbers
        for (int i = 1; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                String str1 = s.substring(0, i);
                String str2 = s.substring(i, j);
                
                if (isValid(str1) && isValid(str2)) {
                    if (check(str1, str2, s.substring(j)))
                        return true;
                }
            }
        }
        return false;
    }

    private boolean isValid(String num) {
        return !(num.length() > 1 && num.startsWith("0"));
    }

    private boolean check(String a, String b, String remaining) {
        if (remaining.length() == 0)
            return true;

        String sum = addStrings(a, b);

        if (!remaining.startsWith(sum))
            return false;

        return check(b, sum, remaining.substring(sum.length()));
    }

    private String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int carry = 0, i = num1.length() - 1, j = num2.length() - 1;

        while (i >= 0 || j >= 0 || carry > 0) {
            int d1 = i >= 0 ? num1.charAt(i--) - '0' : 0;
            int d2 = j >= 0 ? num2.charAt(j--) - '0' : 0;
            int sum = d1 + d2 + carry;
            carry = sum / 10;
            sb.append(sum % 10);
        }

        return sb.reverse().toString();
    }

    // Main method with user input
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string of digits: ");
        String input = sc.nextLine();
        Solution solution = new Solution();
        boolean result = solution.isSumString(input);
        System.out.println("Is sum-string? " + result);
        sc.close();
    }
}
