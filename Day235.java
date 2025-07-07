//Next Greater Element in Circular Array

import java.util.*;

class Solution {
    public ArrayList<Integer> nextLargerElement(int[] arr) {
        int n = arr.length;
        ArrayList<Integer> result = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        int[] nge = new int[n];

        // Initialize all with -1
        for (int i = 0; i < n; i++) {
            nge[i] = -1;
        }

        // Traverse array twice to handle circular nature
        for (int i = 2 * n - 1; i >= 0; i--) {
            int index = i % n;

            while (!stack.isEmpty() && stack.peek() <= arr[index]) {
                stack.pop();
            }

            if (!stack.isEmpty()) {
                nge[index] = stack.peek();
            }

            stack.push(arr[index]);
        }

        for (int val : nge) {
            result.add(val);
        }

        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.print("Enter number of elements in the array: ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        ArrayList<Integer> output = sol.nextLargerElement(arr);

        System.out.println("Next Greater Elements in Circular Array:");
        for (int val : output) {
            System.out.print(val + " ");
        }
    }
}
