//Power of k in factorial of n
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Take input from user
        System.out.print("Enter value of n (1 ≤ n ≤ 10^5): ");
        int n = scanner.nextInt();

        System.out.print("Enter value of k (2 ≤ k ≤ 10^5): ");
        int k = scanner.nextInt();

        Solution sol = new Solution();
        int result = sol.maxKPower(n, k);

        System.out.println("Maximum power x such that " + k + "^x divides " + n + "! is: " + result);
    }
}

class Solution {
    public int maxKPower(int n, int k) {
        Map<Integer, Integer> primeFactors = getPrimeFactors(k);
        int result = Integer.MAX_VALUE;

        for (Map.Entry<Integer, Integer> entry : primeFactors.entrySet()) {
            int p = entry.getKey();
            int a = entry.getValue();
            int count = 0;
            int tempN = n;

            // Legendre’s formula: count how many times p divides n!
            while (tempN > 0) {
                count += tempN / p;
                tempN /= p;
            }

            result = Math.min(result, count / a);
        }

        return result;
    }

    // Prime factorization of k
    private Map<Integer, Integer> getPrimeFactors(int k) {
        Map<Integer, Integer> factors = new HashMap<>();
        for (int i = 2; i * i <= k; i++) {
            while (k % i == 0) {
                factors.put(i, factors.getOrDefault(i, 0) + 1);
                k /= i;
            }
        }
        if (k > 1) {
            factors.put(k, 1);
        }
        return factors;
    }
}
