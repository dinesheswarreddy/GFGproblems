//Remove the balls

import java.util.*;

class Solution {
    public int findLength(int[] color, int[] radius) {
        Stack<int[]> stack = new Stack<>();

        for (int i = 0; i < color.length; i++) {
            if (!stack.isEmpty()) {
                int[] top = stack.peek();
                if (top[0] == color[i] && top[1] == radius[i]) {
                    stack.pop(); // Remove both matching balls
                    continue;
                }
            }
            stack.push(new int[]{color[i], radius[i]});
        }

        return stack.size(); // Remaining balls
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        // User input
        System.out.println("Enter number of balls:");
        int n = sc.nextInt();

        int[] color = new int[n];
        int[] radius = new int[n];

        System.out.println("Enter colors:");
        for (int i = 0; i < n; i++) {
            color[i] = sc.nextInt();
        }

        System.out.println("Enter radii:");
        for (int i = 0; i < n; i++) {
            radius[i] = sc.nextInt();
        }

        int result = sol.findLength(color, radius);
        System.out.println("Remaining balls after user input: " + result);

        // Inbuilt test case
        int[] colorExample = {2, 2, 5};
        int[] radiusExample = {3, 3, 5};
        int resultExample = sol.findLength(colorExample, radiusExample);
        System.out.println("Remaining balls for inbuilt example: " + resultExample);
    }
}
