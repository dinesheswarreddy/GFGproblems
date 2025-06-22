//Largest Divisible Subset

import java.util.*;

class Solution {
    public ArrayList<Integer> largestSubset(int[] arr) {
        Arrays.sort(arr);  // Sort the array

        int n = arr.length;
        List<List<Integer>> dp = new ArrayList<>();

        // Initialize dp with single-element subsets
        for (int num : arr) {
            ArrayList<Integer> initialList = new ArrayList<>();
            initialList.add(num);
            dp.add(initialList);
        }

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] % arr[j] == 0) {
                    List<Integer> candidate = new ArrayList<>(dp.get(j));
                    candidate.add(arr[i]);

                    if (candidate.size() > dp.get(i).size() || 
                        (candidate.size() == dp.get(i).size() && isLexGreater(candidate, dp.get(i)))) {
                        dp.set(i, candidate);
                    }
                }
            }

            // Update result if better subset found
            if (dp.get(i).size() > result.size() ||
                (dp.get(i).size() == result.size() && isLexGreater(dp.get(i), result))) {
                result = dp.get(i);
            }
        }

        return new ArrayList<>(result);
    }

    // Helper to check if list a is lexicographically greater than list b
    private boolean isLexGreater(List<Integer> a, List<Integer> b) {
        int n = Math.min(a.size(), b.size());
        for (int i = 0; i < n; i++) {
            if (!a.get(i).equals(b.get(i))) {
                return a.get(i) > b.get(i);
            }
        }
        return a.size() > b.size();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        // 📥 User Input
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        int[] userArray = new int[n];

        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            userArray[i] = sc.nextInt();
        }

        ArrayList<Integer> userResult = sol.largestSubset(userArray);
        System.out.println("Largest divisible subset from user input: " + userResult);

        // ✅ Inbuilt Example
        int[] builtInExample = {1, 2, 3, 6};
        ArrayList<Integer> builtInResult = sol.largestSubset(builtInExample);
        System.out.println("Largest divisible subset from inbuilt example [1, 2, 3, 6]: " + builtInResult);
    }
}
