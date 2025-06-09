//BST with Dead End

import java.util.*;

class Node {
    int data;
    Node left, right;

    Node(int item) {
        data = item;
        left = right = null;
    }
}

class Solution {
    public boolean isDeadEnd(Node root) {
        return isDeadEndUtil(root, 1, Integer.MAX_VALUE);
    }

    private boolean isDeadEndUtil(Node node, int min, int max) {
        if (node == null) return false;
        if (min == max) return true;
        return isDeadEndUtil(node.left, min, node.data - 1) ||
               isDeadEndUtil(node.right, node.data + 1, max);
    }
}

public class Main {

    // BST insert function
    static Node insert(Node root, int data) {
        if (root == null) return new Node(data);
        if (data < root.data) root.left = insert(root.left, data);
        else if (data > root.data) root.right = insert(root.right, data);
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node root = null;

        System.out.println("Enter number of nodes:");
        int n = sc.nextInt();

        System.out.println("Enter the node values (space separated):");
        for (int i = 0; i < n; i++) {
            int val = sc.nextInt();
            root = insert(root, val);
        }

        Solution sol = new Solution();
        boolean result = sol.isDeadEnd(root);

        System.out.println("Does the BST contain a dead end? " + result);
    }
}
