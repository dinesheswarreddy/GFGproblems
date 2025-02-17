//k largest elements
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Solution {
    // Method to return k largest elements in descending order
    public ArrayList<Integer> kLargest(int[] arr, int k) {
        // Step 1: Sort the array in ascending order
        Arrays.sort(arr);  // Sort in ascending order
        ArrayList<Integer> result = new ArrayList<>();
        
        // Step 2: Take the first `k` elements from the sorted array and add them to the result
        for (int i = arr.length - 1; i >= arr.length - k; i--) {
            result.add(arr[i]);
        }

        // Step 3: Return the result
        return result;
    }

    public static void main(String[] args) {
        // Inbuilt example usage
        Solution solution = new Solution();
        
        // Inbuilt test case
        int[] arr1 = {12, 5, 787, 1, 23};
        int k1 = 2;
        System.out.println("Inbuilt Example:");
        ArrayList<Integer> result1 = solution.kLargest(arr1, k1);
        System.out.println("The " + k1 + " largest elements are: " + result1);
        
        // User input test case
        Scanner scanner = new Scanner(System.in);
        
        // Taking array size and elements as input
        System.out.print("\nEnter the number of elements in the array: ");
        int n = scanner.nextInt();
        int[] arr2 = new int[n];
        
        System.out.print("Enter the elements of the array: ");
        for (int i = 0; i < n; i++) {
            arr2[i] = scanner.nextInt();
        }
        
        // Taking k value as input
        System.out.print("Enter the value of k: ");
        int k2 = scanner.nextInt();
        
        // Calling the kLargest method
        ArrayList<Integer> result2 = solution.kLargest(arr2, k2);
        
        System.out.println("\nUser Input Example:");
        System.out.println("The " + k2 + " largest elements are: " + result2);
        
        scanner.close();
    }
}
