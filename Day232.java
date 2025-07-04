//Subarrays With At Most K Distinct Integers

import java.util.*;

class Solution {
    public int countAtMostK(int arr[], int k) {
        int left = 0, result = 0;
        HashMap<Integer, Integer> freqMap = new HashMap<>();

        for (int right = 0; right < arr.length; right++) {
            freqMap.put(arr[right], freqMap.getOrDefault(arr[right], 0) + 1);

            while (freqMap.size() > k) {
                freqMap.put(arr[left], freqMap.get(arr[left]) - 1);
                if (freqMap.get(arr[left]) == 0) {
                    freqMap.remove(arr[left]);
                }
                left++;
            }

            result += (right - left + 1);
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Enter array elements separated by space (or press Enter to use built-in example):");
        String line = sc.nextLine();

        int[] arr;
        int k;

        if (line.trim().isEmpty()) {
            // Use built-in example
            arr = new int[]{1, 2, 2, 3};
            k = 2;
            System.out.println("Using default example: arr = [1, 2, 2, 3], k = 2");
        } else {
            // Parse user input
            String[] parts = line.trim().split("\\s+");
            arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) {
                arr[i] = Integer.parseInt(parts[i]);
            }

            System.out.print("Enter value of k: ");
            k = sc.nextInt();
        }

        int result = sol.countAtMostK(arr, k);
        System.out.println("Number of subarrays with at most " + k + " distinct integers: " + result);
    }
}
