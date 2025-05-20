//Burning Tree

import java.util.*;
import java.io.*;

class Node {
    int data;
    Node left, right;

    Node(int data) {
        this.data = data;
        left = right = null;
    }
}

public class Solution {

    // Main method to take input and run the solution
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        // Take tree input as a line: e.g. 1 2 3 4 5 N N
        System.out.println("Enter the tree level-order (use 'N' for nulls):");
        String input = sc.nextLine();

        System.out.println("Enter the target node value:");
        int target = sc.nextInt();

        Node root = buildTree(input);

        int result = minTime(root, target);
        System.out.println("Minimum time to burn the entire tree: " + result);
    }

    // Function to build the binary tree from level-order input
    private static Node buildTree(String data) {
        if (data.length() == 0 || data.charAt(0) == 'N') return null;

        String[] parts = data.split(" ");
        Node root = new Node(Integer.parseInt(parts[0]));

        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);

        int i = 1;
        while (!queue.isEmpty() && i < parts.length) {
            Node curr = queue.poll();

            // Left child
            if (!parts[i].equals("N")) {
                curr.left = new Node(Integer.parseInt(parts[i]));
                queue.offer(curr.left);
            }
            i++;

            if (i >= parts.length) break;

            // Right child
            if (!parts[i].equals("N")) {
                curr.right = new Node(Integer.parseInt(parts[i]));
                queue.offer(curr.right);
            }
            i++;
        }

        return root;
    }

    // BFS to simulate burning and return time
    public static int minTime(Node root, int target) {
        Map<Node, Node> parentMap = new HashMap<>();
        Node targetNode = mapParents(root, parentMap, target);

        Queue<Node> queue = new LinkedList<>();
        Set<Node> visited = new HashSet<>();

        queue.offer(targetNode);
        visited.add(targetNode);

        int time = -1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            time++;

            for (int i = 0; i < size; i++) {
                Node current = queue.poll();

                if (current.left != null && !visited.contains(current.left)) {
                    queue.offer(current.left);
                    visited.add(current.left);
                }

                if (current.right != null && !visited.contains(current.right)) {
                    queue.offer(current.right);
                    visited.add(current.right);
                }

                Node parent = parentMap.get(current);
                if (parent != null && !visited.contains(parent)) {
                    queue.offer(parent);
                    visited.add(parent);
                }
            }
        }

        return time;
    }

    // Helper to map child to parent and locate target node
    private static Node mapParents(Node root, Map<Node, Node> parentMap, int target) {
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        Node targetNode = null;

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            if (current.data == target) {
                targetNode = current;
            }

            if (current.left != null) {
                parentMap.put(current.left, current);
                queue.offer(current.left);
            }

            if (current.right != null) {
                parentMap.put(current.right, current);
                queue.offer(current.right);
            }
        }

        return targetNode;
    }
}
