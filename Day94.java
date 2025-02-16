//Serialize and deserialize a binary tree
import java.util.*;
class Tree{
    int data;
    Tree left,right;
    Tree(int d){
        data=d;
        left=right=null;
    }
}
// Define the Tree and Node classes
class Tree {
    static class Node {
        int data;
        Node left, right;
        Node(int d) {
            data = d;
            left = right = null;
        }
    }

    // Function to serialize a tree and return a list containing nodes of the tree.
    public ArrayList<Integer> serialize(Node root) {
        ArrayList<Integer> result = new ArrayList<>();
        if (root == null) return result;
        
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        
        while (!queue.isEmpty()) {
            Node current = queue.poll();
            
            if (current == null) {
                result.add(null);
            } else {
                result.add(current.data);
                queue.add(current.left);
                queue.add(current.right);
            }
        }
        return result;
    }

    // Function to deserialize a list and construct the tree.
    public Node deSerialize(ArrayList<Integer> arr) {
        if (arr == null || arr.isEmpty()) return null;
        
        Queue<Node> queue = new LinkedList<>();
        Node root = new Node(arr.get(0));
        queue.add(root);
        
        int i = 1;
        while (!queue.isEmpty() && i < arr.size()) {
            Node current = queue.poll();
            
            if (arr.get(i) != null) {
                current.left = new Node(arr.get(i));
                queue.add(current.left);
            }
            i++;
            
            if (i < arr.size() && arr.get(i) != null) {
                current.right = new Node(arr.get(i));
                queue.add(current.right);
            }
            i++;
        }
        return root;
    }

    // Helper function for in-order traversal to verify the output.
    public void inorder(Node root) {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }

    // Driver function to test the solution
    public static void main(String[] args) {
        Tree tr = new Tree();  // Create an instance of Tree class

        // Inbuilt Example 1: Root = [1, 2, 3]
        Tree.Node root = new Tree.Node(1);  // Root node with value 1
        root.left = new Tree.Node(2);  // Left child with value 2
        root.right = new Tree.Node(3);  // Right child with value 3
        
        // Serialize and deserialize the inbuilt tree
        System.out.println("Inbuilt Example:");
        ArrayList<Integer> serialized = tr.serialize(root);
        System.out.println("Serialized (Inbuilt): " + serialized);
        
        Tree.Node deserializedRoot = tr.deSerialize(serialized);
        System.out.print("In-order of deserialized tree (Inbuilt): ");
        tr.inorder(deserializedRoot);  // Expected output: 2 1 3
        System.out.println("\n");

        // Take input from the user to create a binary tree
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the binary tree in level order (use -1 for null nodes):");
        ArrayList<Integer> userInput = new ArrayList<>();
        
        // Read the input until user types "done"
        while (sc.hasNextInt()) {
            int value = sc.nextInt();
            if (value == -1) {
                userInput.add(null);  // Use -1 to represent null nodes
            } else {
                userInput.add(value);
            }
        }
        
        // Serialize and deserialize the user-input tree
        Tree.Node userRoot = tr.deSerialize(userInput);
        System.out.println("Serialized (User Input): " + userInput);
        System.out.print("In-order of deserialized tree (User Input): ");
        tr.inorder(userRoot);
        System.out.println();
        
        sc.close(); // Close the scanner
    }
}
