//Counting elements in two arrays

import java.util.*;

class Solution {
    public static ArrayList<Integer> countLessEq(int a[], int b[]) {
        ArrayList<Integer> result = new ArrayList<>();
        Arrays.sort(b); // Sort array b once

        for (int num : a) {
            int count = upperBound(b, num);
            result.add(count);
        }

        return result;
    }

    // Custom upperBound function to find count of elements <= target
    private static int upperBound(int[] arr, int target) {
        int low = 0, high = arr.length;

        while (low < high) {
            int mid = (low + high) / 2;
            if (arr[mid] <= target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // User input
        System.out.print("Enter size of array a: ");
        int n = sc.nextInt();
        int[] a = new int[n];
        System.out.println("Enter elements of array a:");
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        System.out.print("Enter size of array b: ");
        int m = sc.nextInt();
        int[] b = new int[m];
        System.out.println("Enter elements of array b:");
        for (int i = 0; i < m; i++) {
            b[i] = sc.nextInt();
        }

        ArrayList<Integer> result = Solution.countLessEq(a, b);

        System.out.println("Output:");
        for (int val : result) {
            System.out.print(val + " ");
        }

        // Optional: Example built-in test
        System.out.println("\n\nInbuilt test case:");
        int[] testA = {4, 8, 7, 5, 1};
        int[] testB = {4, 48, 3, 0, 1, 1, 5};
        ArrayList<Integer> testResult = Solution.countLessEq(testA, testB);
        System.out.println("Input: a = " + Arrays.toString(testA));
        System.out.println("       b = " + Arrays.toString(testB));
        System.out.println("Output: " + testResult);
    }
}
