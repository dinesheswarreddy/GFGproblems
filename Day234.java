//Maximum Sum Combination
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input array sizes
        System.out.print("Enter size of arrays: ");
        int n = sc.nextInt();

        int[] a = new int[n];
        int[] b = new int[n];

        System.out.println("Enter elements of array a:");
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        System.out.println("Enter elements of array b:");
        for (int i = 0; i < n; i++) {
            b[i] = sc.nextInt();
        }

        System.out.print("Enter value of k: ");
        int k = sc.nextInt();

        Solution sol = new Solution();
        ArrayList<Integer> result = sol.topKSumPairs(a, b, k);

        System.out.println("Top " + k + " maximum sum combinations:");
        for (int sum : result) {
            System.out.print(sum + " ");
        }

        sc.close();
    }
}

// Solution class with method to find top K sum pairs
class Solution {
    public ArrayList<Integer> topKSumPairs(int[] a, int[] b, int k) {
        Arrays.sort(a);
        Arrays.sort(b);
        int n = a.length;

        PriorityQueue<Pair> maxHeap = new PriorityQueue<>((x, y) -> y.sum - x.sum);
        Set<String> visited = new HashSet<>();

        // Start with the max indices
        int i = n - 1, j = n - 1;
        maxHeap.add(new Pair(i, j, a[i] + b[j]));
        visited.add(i + "," + j);

        ArrayList<Integer> result = new ArrayList<>();

        while (k-- > 0 && !maxHeap.isEmpty()) {
            Pair current = maxHeap.poll();
            result.add(current.sum);

            i = current.i;
            j = current.j;

            // Move to (i-1, j)
            if (i - 1 >= 0 && !visited.contains((i - 1) + "," + j)) {
                maxHeap.add(new Pair(i - 1, j, a[i - 1] + b[j]));
                visited.add((i - 1) + "," + j);
            }

            // Move to (i, j-1)
            if (j - 1 >= 0 && !visited.contains(i + "," + (j - 1))) {
                maxHeap.add(new Pair(i, j - 1, a[i] + b[j - 1]));
                visited.add(i + "," + (j - 1));
            }
        }

        return result;
    }

    static class Pair {
        int i, j, sum;

        Pair(int i, int j, int sum) {
            this.i = i;
            this.j = j;
            this.sum = sum;
        }
    }
}
