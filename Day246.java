//LCM Triplet
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Take input from the user
        System.out.print("Enter a number (n): ");
        int n = sc.nextInt();
        
        // Create object of Solution class
        Solution sol = new Solution();
        
        // Call method and print result
        int result = sol.lcmTriplets(n);
        System.out.println("Maximum LCM of any triplet ≤ " + n + " is: " + result);
    }
}

// Solution class as required
class Solution {
    int lcmTriplets(int n) {
        long maxLCM = 0;
        
        // Try all combinations from n to n-4
        for (int i = n; i >= Math.max(1, n - 4); i--) {
            for (int j = n; j >= Math.max(1, n - 4); j--) {
                for (int k = n; k >= Math.max(1, n - 4); k--) {
                    long currentLCM = lcm(lcm(i, j), k);
                    maxLCM = Math.max(maxLCM, currentLCM);
                }
            }
        }
        return (int) maxLCM;
    }

    // LCM using inbuilt GCD
    long lcm(long a, long b) {
        return (a * b) / gcd(a, b);
    }

    // GCD using Euclidean algorithm
    long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
