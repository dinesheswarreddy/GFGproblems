//Pair Sum in BST
import java.util.HashSet;
import java.util.Scanner;

class Solution {
    boolean findTarget(Node root, int target) {
        HashSet<Integer> set = new HashSet<>();
        return findPair(root, set, target);
    }

    private boolean findPair(Node node, HashSet<Integer> set, int target) {
        if (node == null) {
            return false;
        }

        if (set.contains(target - node.data)) {
            return true;
        }

        set.add(node.data);

        return findPair(node.left, set, target) || findPair(node.right, set, target);
    }
}

class Node {
    int data;
    Node left, right;

    Node(int item) {
        data = item;
        left = right = null;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Inbuilt test case
        Node root = new Node(5);
        root.left = new Node(3);
        root.right = new Node(6);
        root.left.left = new Node(2);
        root.left.right = new Node(4);
        root.right.right = new Node(7);
        
        int inbuiltTarget = 9; // Example target for inbuilt test case

        boolean inbuiltResult = solution.findTarget(root, inbuiltTarget);
        System.out.println("Inbuilt test case: " + (inbuiltResult ? "Pair Found" : "No Pair Found"));
        
        // User input test case
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the target value for user input test case: ");
        int userTarget = scanner.nextInt();

        boolean userResult = solution.findTarget(root, userTarget);
        System.out.println("User input test case: " + (userResult ? "Pair Found" : "No Pair Found"));
        
        scanner.close();
    }
}
