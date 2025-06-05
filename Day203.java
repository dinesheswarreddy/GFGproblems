//Count the paths

import java.util.*;

public class Main {

    static class Solution {
        public int countPaths(int[][] edges, int V, int src, int dest) {
            // Step 1: Build adjacency list
            List<List<Integer>> graph = new ArrayList<>();
            for (int i = 0; i < V; i++) graph.add(new ArrayList<>());
            for (int[] edge : edges) {
                graph.get(edge[0]).add(edge[1]);
            }

            // Step 2: Memoization array
            int[] dp = new int[V];
            Arrays.fill(dp, -1);

            // Step 3: Run DFS
            return dfs(graph, src, dest, dp);
        }

        private int dfs(List<List<Integer>> graph, int node, int dest, int[] dp) {
            if (node == dest) return 1;
            if (dp[node] != -1) return dp[node];

            int totalPaths = 0;
            for (int neighbor : graph.get(node)) {
                totalPaths += dfs(graph, neighbor, dest, dp);
            }

            dp[node] = totalPaths;
            return totalPaths;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 🔹 Take input from user
        System.out.print("Enter number of vertices (V): ");
        int V = sc.nextInt();

        System.out.print("Enter number of edges (E): ");
        int E = sc.nextInt();

        int[][] edges = new int[E][2];
        System.out.println("Enter edges in format [u v]:");
        for (int i = 0; i < E; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        System.out.print("Enter source node: ");
        int src = sc.nextInt();

        System.out.print("Enter destination node: ");
        int dest = sc.nextInt();

        Solution sol = new Solution();
        int result = sol.countPaths(edges, V, src, dest);
        System.out.println("Total number of distinct paths from " + src + " to " + dest + ": " + result);

        // 🔸 Example usage with built-in test case
        System.out.println("\n--- Example Test Case ---");
        int[][] testEdges = {{0, 1}, {0, 3}, {2, 0}, {2, 1}, {1, 3}};
        int testV = 4, testSrc = 2, testDest = 3;
        int testResult = sol.countPaths(testEdges, testV, testSrc, testDest);
        System.out.println("Example - Total paths from " + testSrc + " to " + testDest + ": " + testResult);
    }
}
