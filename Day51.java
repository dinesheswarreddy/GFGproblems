//Count all triplets with given sum in sorted array
class Solution {
    public int countTriplets(int[] arr, int target) {
        int count = 0;
        int n = arr.length;
        
        // Loop through the array, fixing the first element (i)
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;
            int total = target - arr[i];
            
            // Use two pointers to find pairs (left, right) such that arr[left] + arr[right] equals total
            while (left < right) {
                if (arr[left] + arr[right] == total) {
                    count++;  // Found a triplet
                    int j = left + 1;
                    
                    // Skip duplicate values from the left pointer
                    while (arr[j] + arr[right] == total) {
                        if (j == right) break;
                        count++;
                        j++;
                    }
                    right--;  // Move right pointer to the left
                } else if (arr[left] + arr[right] > total) {
                    right--;  // Move right pointer left if the sum is too large
                } else {
                    left++;  // Move left pointer right if the sum is too small
                }
            }
        }
        
        return count;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test Case 1
        int[] arr1 = {-3, -1, -1, 0, 1, 2};
        int target1 = -2;
        System.out.println("Test Case 1 Result: " + solution.countTriplets(arr1, target1));  // Expected Output: 4
        
        // Test Case 2
        int[] arr2 = {-2, 0, 1, 1, 5};
        int target2 = 1;
        System.out.println("Test Case 2 Result: " + solution.countTriplets(arr2, target2));  // Expected Output: 0
    }
}
