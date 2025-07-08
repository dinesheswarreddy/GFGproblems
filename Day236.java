//Next element with greater frequency

import java.util.*;

class Solution {
    public ArrayList<Integer> findGreater(int[] arr) {
        int n = arr.length;
        ArrayList<Integer> result = new ArrayList<>();
        Map<Integer, Integer> freq = new HashMap<>();

        // Step 1: Count frequencies
        for (int num : arr) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        Stack<Integer> stack = new Stack<>();
        int[] res = new int[n];

        // Step 2: Traverse from right to left
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && freq.get(stack.peek()) <= freq.get(arr[i])) {
                stack.pop();
            }

            res[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(arr[i]);
        }

        // Convert result to ArrayList
        for (int val : res) {
            result.add(val);
        }

        return result;
    }

    // Helper method to print an array list
    public void printList(ArrayList<Integer> list) {
        for (int val : list) {
            System.out.print(val + " ");
        }
        System.out.println();
    }

    // Main method for testing
    public static void main(String[] args) {
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);

        // --------- USER INPUT ----------
        System.out.println("Enter number of elements:");
        int n = sc.nextInt();
        int[] userArr = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++) {
            userArr[i] = sc.nextInt();
        }

        System.out.println("Output for user input:");
        ArrayList<Integer> userResult = sol.findGreater(userArr);
        sol.printList(userResult);

        // --------- INBUILT EXAMPLE ----------
        int[] builtInArr = {2, 1, 1, 3, 2, 1};
        System.out.println("Output for built-in example: [2, 1, 1, 3, 2, 1]");
        ArrayList<Integer> builtInResult = sol.findGreater(builtInArr);
        sol.printList(builtInResult);
    }
}
