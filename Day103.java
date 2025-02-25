//Histogram Max Rectangular Area
import java.util.*;

class Solution {
    public static int getMaxArea(int arr[]) {
        int n = arr.length;
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        int index = 0;

        while (index < n) {
            if (stack.isEmpty() || arr[stack.peek()] <= arr[index]) {
                stack.push(index++);
            } else {
                int topOfStack = stack.pop();
                int area = arr[topOfStack] * (stack.isEmpty() ? index : index - stack.peek() - 1);
                maxArea = Math.max(maxArea, area);
            }
        }

        while (!stack.isEmpty()) {
            int topOfStack = stack.pop();
            int area = arr[topOfStack] * (stack.isEmpty() ? index : index - stack.peek() - 1);
            maxArea = Math.max(maxArea, area);
        }

        return maxArea;
    }

    public static void main(String[] args) {
        // Inbuilt Example
        int[] arr1 = {60, 20, 50, 40, 10, 50, 60};
        System.out.println("Inbuilt Example Output: " + getMaxArea(arr1));  // Output: 100

        // User Input Example
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of bars in the histogram:");
        int n = scanner.nextInt();
        
        int[] arr2 = new int[n];
        System.out.println("Enter the heights of the bars:");
        for (int i = 0; i < n; i++) {
            arr2[i] = scanner.nextInt();
        }
        
        System.out.println("User Input Example Output: " + getMaxArea(arr2));

        scanner.close();
    }
}
