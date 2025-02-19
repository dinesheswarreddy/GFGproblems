#K Closest Points to Origin
import java.util.*;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // Max Heap to store the k closest points
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(distance(b), distance(a)) // Sort by farthest distance first
        );

        for (int[] point : points) {
            maxHeap.offer(point); // Add the point to the heap
            if (maxHeap.size() > k) {
                maxHeap.poll(); // Remove the farthest point if heap size exceeds k
            }
        }

        // Convert heap to array
        int[][] result = new int[k][2];
        for (int i = 0; i < k; i++) {
            result[i] = maxHeap.poll();
        }
        return result;
    }

    // Helper function to compute squared distance (avoiding sqrt for efficiency)
    private int distance(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }

    // Utility function to print 2D array
    void printPoints(int[][] points) {
        for (int[] point : points) {
            System.out.println(Arrays.toString(point));
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Inbuilt Example: Finding the 3 closest points to the origin (0, 0)
        int[][] points = {
            {1, 3}, {3, 3}, {5, -1}, {-2, 4}, {2, -2}
        };
        int k = 3;

        System.out.println("Inbuilt Example:");
        int[][] closestPoints = sol.kClosest(points, k);
        sol.printPoints(closestPoints);  // Expected output: 3 closest points to origin

        // User input example:
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of points: ");
        int n = scanner.nextInt();
        int[][] userPoints = new int[n][2];

        System.out.println("Enter the points (x, y): ");
        for (int i = 0; i < n; i++) {
            userPoints[i][0] = scanner.nextInt(); // x-coordinate
            userPoints[i][1] = scanner.nextInt(); // y-coordinate
        }

        System.out.println("Enter the value of k: ");
        int userK = scanner.nextInt();

        int[][] userClosestPoints = sol.kClosest(userPoints, userK);
        System.out.println("User Input Example:");
        sol.printPoints(userClosestPoints);  // Output will depend on user input
    }
}
