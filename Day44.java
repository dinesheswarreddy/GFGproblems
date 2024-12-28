//Find All Triplets with Zero Sum
import java.util.*;

class Solution {
    public List<List<Integer>> findTriplets(int[] arr) {
        List<List<Integer>> result = new ArrayList<>();
        int n = arr.length;

        // Iterate through all possible triplets
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (arr[i] + arr[j] + arr[k] == 0) {
                        result.add(Arrays.asList(i, j, k));
                    }
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        int[] arr1 = {0, -1, 2, -3, 1};
        List<List<Integer>> result1 = solution.findTriplets(arr1);
        System.out.println("Triplets for arr1: " + result1); // Expected: [[0, 1, 4], [2, 3, 4]]

        // Test case 2
        int[] arr2 = {1, -2, 1, 0, 5};
        List<List<Integer>> result2 = solution.findTriplets(arr2);
        System.out.println("Triplets for arr2: " + result2); // Expected: [[0, 1, 2]]

        // Test case 3
        int[] arr3 = {2, 3, 1, 0, 5};
        List<List<Integer>> result3 = solution.findTriplets(arr3);
        System.out.println("Triplets for arr3: " + result3); // Expected: []

    }
}
