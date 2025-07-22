//Smallest Positive Missing
import java.util.Scanner;

class Solution {
    public int missingNumber(int[] arr) {
        int n = arr.length;

        // Place each number in its correct position
        for (int i = 0; i < n; i++) {
            while (arr[i] > 0 && arr[i] <= n && arr[arr[i] - 1] != arr[i]) {
                int correctIndex = arr[i] - 1;
                int temp = arr[i];
                arr[i] = arr[correctIndex];
                arr[correctIndex] = temp;
            }
        }

        // Find the first index where arr[i] != i + 1
        for (int i = 0; i < n; i++) {
            if (arr[i] != i + 1) {
                return i + 1;
            }
        }

        // All numbers from 1 to n are present
        return n + 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Take array size input
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();

        // Take array elements input
        int[] arr = new int[n];
        System.out.println("Enter the array elements (space separated):");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        // Create object and call method
        Solution solution = new Solution();
        int missing = solution.missingNumber(arr);

        // Output the result
        System.out.println("Smallest positive missing number: " + missing);

        scanner.close();
    }
}
