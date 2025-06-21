//Police and Thieves

import java.util.*;

class Solution {
    public int catchThieves(char[] arr, int k) {
        int n = arr.length;
        Queue<Integer> police = new LinkedList<>();
        Queue<Integer> thief = new LinkedList<>();
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] == 'P') {
                police.add(i);
            } else if (arr[i] == 'T') {
                thief.add(i);
            }

            while (!police.isEmpty() && !thief.isEmpty()) {
                int p = police.peek();
                int t = thief.peek();
                
                if (Math.abs(p - t) <= k) {
                    count++;
                    police.poll();
                    thief.poll();
                } else if (t < p) {
                    thief.poll();
                } else {
                    police.poll();
                }
            }
        }
        return count;
    }

    // Main method with user input and example usage
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution sol = new Solution();

        // User input
        System.out.println("Enter array elements (e.g. P T T P T):");
        String[] inputArr = scanner.nextLine().split(" ");
        char[] arr = new char[inputArr.length];
        for (int i = 0; i < inputArr.length; i++) {
            arr[i] = inputArr[i].charAt(0);
        }

        System.out.print("Enter the value of k: ");
        int k = scanner.nextInt();

        int result = sol.catchThieves(arr, k);
        System.out.println("Maximum thieves caught: " + result);

        // Example inbuilt test case
        char[] testArr = {'T', 'T', 'P', 'P', 'T', 'P'};
        int testK = 2;
        System.out.println("\nRunning inbuilt test case:");
        System.out.println("Input: " + Arrays.toString(testArr) + ", k = " + testK);
        int testResult = sol.catchThieves(testArr, testK);
        System.out.println("Expected output: 3");
        System.out.println("Actual output: " + testResult);
    }
}
