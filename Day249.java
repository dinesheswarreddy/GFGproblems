//Count the Coprimes

import java.util.*;

public class Solution {
    static final int MAX = 10001;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Example 1: Hardcoded array
        int[] exampleArr = {4, 8, 3, 9};
        System.out.println("Example 1 - Hardcoded Input: " + Arrays.toString(exampleArr));
        System.out.println("Coprime Pairs: " + cntCoprime(exampleArr));
        System.out.println();

        // Example 2: Take input from user
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int[] userArr = new int[n];
        System.out.print("Enter elements: ");
        for (int i = 0; i < n; i++) {
            userArr[i] = sc.nextInt();
        }

        System.out.println("Coprime Pairs: " + cntCoprime(userArr));
    }

    // Main logic using Möbius inversion
    static int cntCoprime(int[] arr) {
        int[] freq = new int[MAX];
        for (int val : arr) freq[val]++;

        int[] f = new int[MAX];
        for (int d = 1; d < MAX; d++) {
            for (int mult = d; mult < MAX; mult += d) {
                f[d] += freq[mult];
            }
        }

        int[] mu = mobius(MAX);

        long result = 0;
        for (int d = 1; d < MAX; d++) {
            if (f[d] >= 2) {
                long pairs = (long) f[d] * (f[d] - 1) / 2;
                result += mu[d] * pairs;
            }
        }

        return (int) result;
    }

    // Sieve for Möbius function
    static int[] mobius(int n) {
        int[] mu = new int[n];
        Arrays.fill(mu, 1);
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);

        for (int i = 2; i < n; i++) {
            if (isPrime[i]) {
                for (int j = i; j < n; j += i) {
                    mu[j] *= -1;
                    isPrime[j] = false;
                }
                for (int j = i * i; j < n; j += i * i) {
                    mu[j] = 0;
                }
            }
        }

        mu[0] = 0;
        return mu;
    }
}
