#Count pairs with given sum
import java.util.HashMap;

public class PairSum {

    // Function to count pairs whose sum equals the target
    public static int countPairs(int arr[], int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;

        for (int num : arr) {
            int complement = target - num;
            if (map.containsKey(complement)) {
                count += map.get(complement);
            }
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        return count;
    }

    public static void main(String[] args) {
        // Example usage:
        int arr[] = {1, 5, 7, -1, 5};
        int target = 6;

        // Calling the function and printing the result
        int result = countPairs(arr, target);
        System.out.println("Number of pairs with sum " + target + " is: " + result);
    }
}
