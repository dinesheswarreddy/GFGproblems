//Predecessor and Successor

import java.util.*;

// Definition of BST Node
class Node {
    int data;
    Node left, right;
    Node(int x) {
        data = x;
        left = right = null;
    }
}

class Solution {
    Node pre = null, suc = null;

    public ArrayList<Node> findPreSuc(Node root, int key) {
        pre = null;
        suc = null;
        find(root, key);
        ArrayList<Node> result = new ArrayList<>();
        result.add(pre != null ? pre : null);
        result.add(suc != null ? suc : null);
        return result;
    }

    private void find(Node root, int key) {
        if (root == null) return;

        if (root.data == key) {
            if (root.left != null) {
                Node temp = root.left;
                while (temp.right != null) temp = temp.right;
                pre = temp;
            }
            if (root.right != null) {
                Node temp = root.right;
                while (temp.left != null) temp = temp.left;
                suc = temp;
            }
        } else if (key < root.data) {
            suc = root;
            find(root.left, key);
        } else {
            pre = root;
            find(root.right, key);
        }
    }
}

public class Main {

    // Insert into BST
    public static Node insert(Node root, int key) {
        if (root == null) return new Node(key);
        if (key < root.data) root.left = insert(root.left, key);
        else root.right = insert(root.right, key);
        return root;
    }

    // Build BST from list
    public static Node buildBST(int[] values) {
        Node root = null;
        for (int val : values) {
            root = insert(root, val);
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Example 1: Predefined BST
        int[] values = {8, 1, 9, 4, 3, 10};
        Node root = buildBST(values);
        int key = 8;

        Solution sol = new Solution();
        ArrayList<Node> result = sol.findPreSuc(root, key);
        System.out.println("Example 1:");
        System.out.println("Predecessor of " + key + ": " + (result.get(0) != null ? result.get(0).data : "NULL"));
        System.out.println("Successor of " + key + ": " + (result.get(1) != null ? result.get(1).data : "NULL"));

        // Example 2: User Input
        System.out.println("\nCustom Input:");
        System.out.print("Enter number of nodes: ");
        int n = sc.nextInt();
        int[] userValues = new int[n];
        System.out.print("Enter BST elements (space separated): ");
        for (int i = 0; i < n; i++) userValues[i] = sc.nextInt();

        Node userRoot = buildBST(userValues);

        System.out.print("Enter key to find predecessor and successor: ");
        int userKey = sc.nextInt();

        ArrayList<Node> userResult = sol.findPreSuc(userRoot, userKey);
        System.out.println("Predecessor of " + userKey + ": " + (userResult.get(0) != null ? userResult.get(0).data : "NULL"));
        System.out.println("Successor of " + userKey + ": " + (userResult.get(1) != null ? userResult.get(1).data : "NULL"));
    }
}
