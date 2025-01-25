//Find the first node of loop in linked list
import java.util.Scanner;

class Node {
    int data;
    Node next;
    
    Node(int x) {
        data = x;
        next = null;
    }
}

class Solution {
    public static Node findFirstNode(Node head) {
        // Step 1: Initialize two pointers (slow and fast)
        Node slow = head;
        Node fast = head;
        
        // Step 2: Detect loop using Floyd's cycle-finding algorithm
        while (fast != null && fast.next != null) {
            slow = slow.next;             // Move slow pointer one step
            fast = fast.next.next;        // Move fast pointer two steps
            
            if (slow == fast) {  // Loop detected
                // Step 3: Find the starting node of the loop
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;  // Return the first node of the loop
            }
        }
        
        // No loop found, return null
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        // Example 1: Inbuilt list with a loop (hardcoded)
        Node head1 = new Node(1);
        head1.next = new Node(2);
        head1.next.next = new Node(3);
        head1.next.next.next = new Node(4);
        head1.next.next.next.next = new Node(5);
        head1.next.next.next.next.next = head1.next.next;  // Creates a loop at node 3

        Node loopStart1 = Solution.findFirstNode(head1);
        if (loopStart1 != null) {
            System.out.println("Inbuilt Example: Loop starts at node with data: " + loopStart1.data);
        } else {
            System.out.println("Inbuilt Example: No loop detected");
        }

        // Example 2: List created using user input
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter number of nodes in the linked list:");
        int n = sc.nextInt();
        
        if (n <= 0) {
            System.out.println("Invalid input! List cannot have 0 or negative nodes.");
            return;
        }
        
        System.out.println("Enter the node values:");
        Node head2 = new Node(sc.nextInt());
        Node temp = head2;
        
        for (int i = 1; i < n; i++) {
            Node newNode = new Node(sc.nextInt());
            temp.next = newNode;
            temp = newNode;
        }
        
        System.out.println("Enter the position of the node to which the last node should point to (1-based index):");
        int pos = sc.nextInt();
        
        if (pos > 0) {
            Node loopNode = head2;
            int index = 1;
            while (index < pos && loopNode != null) {
                loopNode = loopNode.next;
                index++;
            }
            if (loopNode != null) {
                temp.next = loopNode;  // Create the loop by connecting the last node to the node at position 'pos'
            }
        }
        
        Node loopStart2 = Solution.findFirstNode(head2);
        if (loopStart2 != null) {
            System.out.println("User Input Example: Loop starts at node with data: " + loopStart2.data);
        } else {
            System.out.println("User Input Example: No loop detected");
        }
        
        sc.close();
    }
}
