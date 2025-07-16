//Nine Divisors

import java.util.*;

public class Solution {
    public static int countNumbers(int n) {
        List<Integer> primes = sieve((int)Math.sqrt(n) + 1);
        int count = 0;

        // Case 1: Numbers of form p^8
        for (int p : primes) {
            long num = 1;
            for (int i = 0; i < 8; i++) {
                num *= p;
                if (num > n) break;
            }
            if (Math.pow(p, 8) <= n) count++;
        }

        // Case 2: Numbers of form p^2 * q^2
        int size = primes.size();
        for (int i = 0; i < size; i++) {
            long p2 = (long)primes.get(i) * primes.get(i);
            if (p2 > n) break;
            for (int j = i + 1; j < size; j++) {
                long q2 = (long)primes.get(j) * primes.get(j);
                if (p2 * q2 <= n) {
                    count++;
                } else {
                    break;
                }
            }
        }

        return count;
    }

    private static List<Integer> sieve(int limit) {
        boolean[] isPrime = new boolean[limit + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i * i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= limit; i++) {
            if (isPrime[i]) primes.add(i);
        }

        return primes;
    }

    // Main method with user input and test cases
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // User input
        System.out.print("Enter a number n: ");
        int n = scanner.nextInt();

        // Result from user input
        int result = countNumbers(n);
        System.out.println("Count of numbers with exactly 9 divisors <= " + n + ": " + result);

        // Inbuilt test cases
        System.out.println("\n--- Inbuilt Test Cases ---");
        System.out.println("Input: 100 → Output: " + countNumbers(100));   // Output: 2
        System.out.println("Input: 200 → Output: " + countNumbers(200));   // Output: 3

        scanner.close();
    }
}
