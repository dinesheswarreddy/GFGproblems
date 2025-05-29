//Sum of nodes on the longest path

import java.util.*;

// Tree node class
class Node {
    int data;
    Node left, right;

    Node(int data) {
        this.data = data;
    }
}

// Main Solution class
class Solution {
    static class Result {
        int maxLen;
        int maxSum;

        Result(int maxLen, int maxSum) {
            this.maxLen = maxLen;
            this.maxSum = maxSum;
        }
    }

    public int sumOfLongRootToLeafPath(Node root) {
        Result res = helper(root);
        return res.maxSum;
    }

    private Result helper(Node node) {
        if (node == null)
            return new Result(0, 0);

        Result left = helper(node.left);
        Result right = helper(node.right);

        if (left.maxLen > right.maxLen) {
            return new Result(left.maxLen + 1, left.maxSum + node.data);
        } else if (right.maxLen > left.maxLen) {
            return new Result(right.maxLen + 1, right.maxSum + node.data);
        } else {
            int maxSum = Math.max(left.maxSum, right.maxSum);
            return new Result(left.maxLen + 1, maxSum + node.data);
        }
    }
}

// Utility class to build tree from input
class TreeBuilder {
    public static Node buildTree(String[] input) {
        if (input.length == 0 || input[0].equals("N"))
            return null;

        Node root = new Node(Integer.parseInt(input[0]));
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        int i = 1;
        while (!queue.isEmpty() && i < input.length) {
            Node current = queue.poll();

            if (!input[i].equals("N")) {
                current.left = new Node(Integer.parseInt(input[i]));
                queue.add(current.left);
            }
            i++;
            if (i >= input.length) break;

            if (!input[i].equals("N")) {
                current.right = new Node(Integer.parseInt(input[i]));
                queue.add(current.right);
            }
            i++;
        }

        return root;
    }
}

// Driver class
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the binary tree in level order (use N for null):");
        String inputLine = scanner.nextLine();
        String[] input = inputLine.trim().split("\\s+");

        Node root = TreeBuilder.buildTree(input);

        Solution solution = new Solution();
        int result = solution.sumOfLongRootToLeafPath(root);
        System.out.println("Sum of the longest root-to-leaf path: " + result);
    }
}
