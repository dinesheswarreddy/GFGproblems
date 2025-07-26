//Majority Element - More Than n/3

import java.util.*;

class Solution {
    public ArrayList<Integer> findMajority(int[] arr) {
        int n = arr.length;
        Integer candidate1 = null, candidate2 = null;
        int count1 = 0, count2 = 0;

        // Step 1: Find potential candidates
        for (int num : arr) {
            if (candidate1 != null && num == candidate1) {
                count1++;
            } else if (candidate2 != null && num == candidate2) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = num;
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = num;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        // Step 2: Validate the candidates
        count1 = 0;
        count2 = 0;
        for (int num : arr) {
            if (candidate1 != null && num == candidate1) count1++;
            else if (candidate2 != null && num == candidate2) count2++;
        }

        ArrayList<Integer> result = new ArrayList<>();
        int threshold = n / 3;
        if (count1 > threshold) result.add(candidate1);
        if (count2 > threshold) result.add(candidate2);

        Collections.sort(result);  // Return sorted output
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Example: Enter size and array elements
        System.out.print("Enter size of array: ");
        int n = sc.nextInt();

        int[] arr = new int[n];
        System.out.print("Enter " + n + " elements: ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Solution sol = new Solution();
        ArrayList<Integer> res = sol.findMajority(arr);

        System.out.println("Majority elements (> floor(n/3)) are: " + res);
    }
}
