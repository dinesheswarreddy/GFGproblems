//Longest subarray with Atmost two distinct integers
import java.util.*;

public class Solution {
    // Function to find the longest subarray with at most 2 distinct integers
    public int totalElements(int[] arr) {
        int start = 0, maxLen = 0;
        Map<Integer, Integer> map = new HashMap<>();

        for (int end = 0; end < arr.length; end++) {
            map.put(arr[end], map.getOrDefault(arr[end], 0) + 1);

            while (map.size() > 2) {
                map.put(arr[start], map.get(arr[start]) - 1);
                if (map.get(arr[start]) == 0) {
                    map.remove(arr[start]);
                }
                start++;
            }

            maxLen = Math.max(maxLen, end - start + 1);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        // ✅ User Input Example
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        int[] userArray = new int[n];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            userArray[i] = sc.nextInt();
        }

        int userResult = sol.totalElements(userArray);
        System.out.println("Longest subarray with at most two distinct integers (user input): " + userResult);

        // ✅ Inbuilt Example
        int[] inbuiltArray = {3, 1, 2, 2, 2, 2};
        int inbuiltResult = sol.totalElements(inbuiltArray);
        System.out.println("Longest subarray with at most two distinct integers (inbuilt test): " + inbuiltResult);
    }
}
