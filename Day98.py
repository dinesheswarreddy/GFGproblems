#Find median in a stream
import java.util.*;

class Solution {
    public ArrayList<Double> getMedian(int[] arr) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        ArrayList<Double> medians = new ArrayList<>();
        
        for (int num : arr) {
            maxHeap.add(num);
            
            if (!minHeap.isEmpty() && maxHeap.peek() > minHeap.peek()) {
                minHeap.add(maxHeap.poll());
            }
            
            if (maxHeap.size() > minHeap.size() + 1) {
                minHeap.add(maxHeap.poll());
            } else if (minHeap.size() > maxHeap.size()) {
                maxHeap.add(minHeap.poll());
            }
            
            if (maxHeap.size() > minHeap.size()) {
                medians.add((double) maxHeap.peek());
            } else {
                medians.add((maxHeap.peek() + minHeap.peek()) / 2.0);
            }
        }
        
        return medians;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Example 1: Inbuilt array
        int[] arr1 = {5, 15, 1, 3, 2, 8};
        System.out.println("Median for inbuilt array: " + solution.getMedian(arr1));
        
        // Example 2: Input from user
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of elements:");
        int n = scanner.nextInt();
        
        int[] arr2 = new int[n];
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr2[i] = scanner.nextInt();
        }
        
        System.out.println("Median for user input array: " + solution.getMedian(arr2));
        
        scanner.close();
    }
}
