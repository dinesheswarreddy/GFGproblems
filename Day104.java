//Maximum of minimum for every window size
import java.util.*;

class Solution {
    public ArrayList<Integer> maxOfMins(int[] arr) {
        int n = arr.length;
        
        int[] pse = new int[n];
        int[] nse = new int[n];
        
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            pse[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        
        stack.clear();
        
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            nse[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        
        int[] result = new int[n + 1];
        
        for (int i = 0; i < n; i++) {
            int len = nse[i] - pse[i] - 1;
            result[len] = Math.max(result[len], arr[i]);
        }
        
        for (int i = n - 1; i >= 1; i--) {
            result[i] = Math.max(result[i], result[i + 1]);
        }
        
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            res.add(result[i]);
        }
        
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Example 1: Inbuilt example
        int[] arr1 = {10, 20, 30, 50, 10, 70, 30};
        System.out.println("Result for inbuilt array: " + sol.maxOfMins(arr1));
        
        // Example 2: User input example
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int size = sc.nextInt();
        
        int[] arr2 = new int[size];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < size; i++) {
            arr2[i] = sc.nextInt();
        }
        
        System.out.println("Result for user input array: " + sol.maxOfMins(arr2));
    }
}
