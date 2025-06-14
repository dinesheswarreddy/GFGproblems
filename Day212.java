//Symmetric Tree

import java.util.*;

class Node {
    int data;
    Node left, right;

    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Solution {
    public boolean isSymmetric(Node root) {
        if (root == null) return true;
        return isMirror(root.left, root.right);
    }

    private boolean isMirror(Node left, Node right) {
        if (left == null && right == null) return true;
        if (left == null || right == null) return false;
        if (left.data != right.data) return false;

        return isMirror(left.left, right.right) && isMirror(left.right, right.left);
    }
}

public class Main {
    // Helper function to build tree from level-order input
    public static Node buildTree(String[] nodes) {
        if (nodes.length == 0 || nodes[0].equals("N")) return null;

        Node root = new Node(Integer.parseInt(nodes[0]));
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        int i = 1;
        while (!queue.isEmpty() && i < nodes.length) {
            Node current = queue.poll();

            // Left child
            if (!nodes[i].equals("N")) {
                current.left = new Node(Integer.parseInt(nodes[i]));
                queue.add(current.left);
            }
            i++;

            if (i >= nodes.length) break;

            // Right child
            if (!nodes[i].equals("N")) {
                current.right = new Node(Integer.parseInt(nodes[i]));
                queue.add(current.right);
            }
            i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input format: Level-order traversal, e.g., 1 2 2 3 4 4 3
        System.out.println("Enter tree nodes in level order (use N for null):");
        String[] input = sc.nextLine().split(" ");

        Node root = buildTree(input);

        Solution sol = new Solution();
        boolean result = sol.isSymmetric(root);
        System.out.println("Is the tree symmetric? " + result);
    }
}
