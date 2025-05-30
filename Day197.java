//Closest Neighbour in BST
import java.util.*;

// Node class definition
class Node {
    int data;
    Node left, right;

    Node(int x) {
        data = x;
        left = right = null;
    }
}

class Solution {
    // Function to find the closest (<=k) value in BST
    public int findMaxFork(Node root, int k) {
        int result = -1; // If no value found ≤ k
        while (root != null) {
            if (root.data <= k) {
                result = root.data;
                root = root.right;
            } else {
                root = root.left;
            }
        }
        return result;
    }
}

public class Main {

    // Function to insert a node in BST
    public static Node insert(Node root, int key) {
        if (root == null) return new Node(key);
        if (key < root.data) root.left = insert(root.left, key);
        else root.right = insert(root.right, key);
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node root = null;

        System.out.println("Enter the number of nodes:");
        int n = sc.nextInt();

        System.out.println("Enter the node values (space separated):");
        for (int i = 0; i < n; i++) {
            int val = sc.nextInt();
            root = insert(root, val);
        }

        System.out.println("Enter value of k:");
        int k = sc.nextInt();

        Solution sol = new Solution();
        int result = sol.findMaxFork(root, k);

        System.out.println("Greatest value <= " + k + " in BST is: " + result);
    }
}
