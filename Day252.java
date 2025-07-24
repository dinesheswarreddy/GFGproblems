//Last Moment Before All Ants Fall Out

import java.util.Scanner;

class Solution {

    public int getLastMoment(int n, int left[], int right[]) {
        int maxTime = 0;

        for (int pos : left) {
            maxTime = Math.max(maxTime, pos); // Time to fall off left end
        }

        for (int pos : right) {
            maxTime = Math.max(maxTime, n - pos); // Time to fall off right end
        }

        return maxTime;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Choose mode:\n1. User Input\n2. Inbuilt Example");
        int choice = sc.nextInt();

        if (choice == 1) {
            // === User Input ===
            System.out.print("Enter length of the plank (n): ");
            int n = sc.nextInt();

            System.out.print("Enter number of ants moving left: ");
            int l = sc.nextInt();
            int[] left = new int[l];
            System.out.print("Enter positions of ants moving left: ");
            for (int i = 0; i < l; i++) {
                left[i] = sc.nextInt();
            }

            System.out.print("Enter number of ants moving right: ");
            int r = sc.nextInt();
            int[] right = new int[r];
            System.out.print("Enter positions of ants moving right: ");
            for (int i = 0; i < r; i++) {
                right[i] = sc.nextInt();
            }

            int result = sol.getLastMoment(n, left, right);
            System.out.println("Last moment before all ants fall off: " + result);

        } else {
            // === Inbuilt Test Case ===
            int n = 4;
            int[] left = {2};
            int[] right = {0, 1, 3};

            System.out.println("Using inbuilt example:");
            System.out.println("n = " + n);
            System.out.print("left[] = ");
            for (int x : left) System.out.print(x + " ");
            System.out.print("\nright[] = ");
            for (int x : right) System.out.print(x + " ");
            System.out.println();

            int result = sol.getLastMoment(n, left, right);
            System.out.println("Last moment before all ants fall off: " + result);
        }

        sc.close();
    }
}
