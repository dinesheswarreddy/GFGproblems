//Pythagorean Triplet

import java.util.*;

class Solution {
    boolean pythagoreanTriplet(int[] arr) {
        if (arr.length < 2) {
            return false;
        }

        HashSet<Integer> hs = new HashSet<>();

        for (int num : arr) {
            hs.add(num);
        }

        for (int i = 0; i < arr.length; i++) {
            int a = arr[i];

            for (int j = i + 1; j < arr.length; j++) {
                int b = arr[j];

                int root = (int) Math.sqrt(a * a + b * b);

                if (hs.contains(root) && root * root == a * a + b * b) {
                    return true;
                }
            }
        }
        return false;
    }

    // Driver code for user input + example usage
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        // ==== Example usage ====
        int[] testArr = {3, 2, 4, 6, 5};
        System.out.println("Example Test: " + Arrays.toString(testArr));
        System.out.println("Has Pythagorean Triplet? " + sol.pythagoreanTriplet(testArr));

        // ==== User Input ====
        System.out.print("\nEnter number of elements: ");
        int n = sc.nextInt();
        int[] userArr = new int[n];

        System.out.println("Enter array elements:");
        for (int i = 0; i < n; i++) {
            userArr[i] = sc.nextInt();
        }

        System.out.println("Has Pythagorean Triplet? " + sol.pythagoreanTriplet(userArr));
    }
}
