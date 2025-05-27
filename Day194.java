//Print leaf nodes from preorder traversal of BST

import java.util.*;

class Solution {
    public ArrayList<Integer> leafNodes(int[] preorder) {
        Stack<Integer> stk = new Stack<>();
        int n = preorder.length;
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            if (stk.isEmpty()) stk.push(preorder[i]);
            else {
                if (stk.peek() < preorder[i]) {
                    int storage = stk.peek();
                    int counter = 0;
                    while (!stk.isEmpty() && stk.peek() < preorder[i]) {
                        counter++;
                        stk.pop();
                    }
                    if (counter >= 2) {
                        res.add(storage);
                    }
                }
                stk.push(preorder[i]);
            }
        }
        if (!stk.isEmpty()) res.add(stk.peek());
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // ---------- USER INPUT ----------
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements in preorder traversal: ");
        int n = sc.nextInt();
        int[] preorder = new int[n];
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            preorder[i] = sc.nextInt();
        }
        ArrayList<Integer> result = sol.leafNodes(preorder);
        System.out.println("Leaf nodes: " + result);

        // ---------- INBUILT TEST CASE ----------
        int[] testPreorder = {4, 2, 1, 3, 6, 5};
        System.out.println("\nInbuilt Test Case:");
        System.out.println("Input: " + Arrays.toString(testPreorder));
        System.out.println("Leaf nodes: " + sol.leafNodes(testPreorder));
    }
}
