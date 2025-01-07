//Pair with given sum in a sorted array
import java.io.*;
import java.lang.*;
import java.util.*;

class Solution {
    int countPairs(int arr[], int target) {
        HashMap<Integer, Integer> h = new HashMap<>();
        int count = 0;
        for (int i : arr) {
            int sum = target - i;
            if (h.containsKey(sum)) {
                count += h.get(sum);
            }
            h.put(i, h.getOrDefault(i, 0) + 1);
        }
        return count;
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        System.out.println("Enter the number of test cases:");
        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            System.out.println("Enter the array elements (space-separated):");
            String[] inputLine = br.readLine().trim().split(" ");
            int[] arr = new int[inputLine.length];
            for (int i = 0; i < inputLine.length; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            System.out.println("Enter the target sum:");
            int target = Integer.parseInt(br.readLine().trim());

            Solution obj = new Solution();
            int res = obj.countPairs(arr, target);
            System.out.println("Number of pairs: " + res);
            System.out.println("~");
        }
        
        // Predefined Example
        System.out.println("Predefined Example:");
        int[] predefinedArr = {-1, 1, 5, 5, 7};
        int predefinedTarget = 6;
        Solution obj2 = new Solution();
        int predefinedRes = obj2.countPairs(predefinedArr, predefinedTarget);
        System.out.println("Number of pairs: " + predefinedRes);
        System.out.println("~");
    }
}
