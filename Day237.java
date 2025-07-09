//Sum of subarray minimum
import java.util.*;

public class Main {

    public static int sumSubMins(int[] arr) {
        int MOD = (int)1e9 + 7;
        int n = arr.length;
        int[] prev = new int[n];
        int[] next = new int[n];

        Stack<Integer> stack = new Stack<>();

        // Previous Less Element
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            prev[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }

        stack.clear();

        // Next Less Element
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            next[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }

        long sum = 0;
        for (int i = 0; i < n; i++) {
            long count = (long)(i - prev[i]) * (next[i] - i);
            sum = (sum + arr[i] * count) % MOD;
        }

        return (int)sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // --- User Input ---
        System.out.println("Enter size of the array:");
        int n = sc.nextInt();
        int[] userArr = new int[n];
        System.out.println("Enter " + n + " elements:");
        for (int i = 0; i < n; i++) {
            userArr[i] = sc.nextInt();
        }
        int userResult = sumSubMins(userArr);
        System.out.println("Sum of subarray minimums (User Input): " + userResult);

        // --- Inbuilt Example ---
        int[] inbuiltArr = {3, 1, 2, 4};
        int inbuiltResult = sumSubMins(inbuiltArr);
        System.out.println("Sum of subarray minimums (Inbuilt Example [3,1,2,4]): " + inbuiltResult);
    }
}
