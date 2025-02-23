//Next Greater Element
import java.util.*;

class Solution {
    // Function to find the next greater element for each element of the array.
    public ArrayList<Integer> nextLargerElement(int[] arr) {
        int n = arr.length;
        ArrayList<Integer> result = new ArrayList<>(Collections.nCopies(n, -1)); // Initialize result with -1
        Stack<Integer> stack = new Stack<>();

        // Traverse the array
        for (int i = 0; i < n; i++) {
            // While the stack is not empty and the current element is greater than the element at stack's top
            while (!stack.isEmpty() && arr[i] > arr[stack.peek()]) {
                int index = stack.pop();
                result.set(index, arr[i]); // Set the next greater element for arr[index]
            }
            stack.push(i); // Push current index to the stack
        }
        
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Solution solution = new Solution();

        // Inbuilt example
        System.out.println("Inbuilt Example:");
        int[] arrInbuilt = {1, 3, 2, 4};
        ArrayList<Integer> resultInbuilt = solution.nextLargerElement(arrInbuilt);
        System.out.println(resultInbuilt);

        // User input example
        System.out.println("\nEnter the number of elements in the array:");
        int n = scanner.nextInt();
        int[] arrUser = new int[n];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            arrUser[i] = scanner.nextInt();
        }

        ArrayList<Integer> resultUser = solution.nextLargerElement(arrUser);
        System.out.println("\nNext Greater Element for the input array:");
        System.out.println(resultUser);
        
        scanner.close();
    }
}
