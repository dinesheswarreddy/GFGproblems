//Remove loop in Linked List
import java.util.Scanner;

class Node {
    int data;
    Node next;
}

class Solution {
    public static void removeLoop(Node head) {
        if (head == null || head.next == null) {
            return;
        }

        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                break;
            }
        }

        if (slow != fast) {
            return;
        }

        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }

        Node prev = null;
        while (fast.next != slow) {
            fast = fast.next;
        }

        fast.next = null;
    }

    // Helper function to create a new node
    public static Node createNode(int data) {
        Node newNode = new Node();
        newNode.data = data;
        newNode.next = null;
        return newNode;
    }

    // Helper function to print the list
    public static void printList(Node head) {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Example 1: User input
        System.out.println("Enter the number of nodes:");
        int n = scanner.nextInt();
        Node head = null;
        Node temp = null;

        // Create linked list from user input
        for (int i = 0; i < n; i++) {
            System.out.println("Enter data for node " + (i + 1) + ":");
            int data = scanner.nextInt();
            Node newNode = createNode(data);

            if (head == null) {
                head = newNode;
            } else {
                temp.next = newNode;
            }
            temp = newNode;
        }

        System.out.println("Enter the position (1-based) where last node should point to (0 for no loop):");
        int pos = scanner.nextInt();
        
        if (pos > 0) {
            Node loopNode = head;
            int count = 1;
            while (count < pos && loopNode != null) {
                loopNode = loopNode.next;
                count++;
            }
            temp.next = loopNode; // Create a loop
        }

        System.out.println("Before removing loop:");
        printList(head);
        Solution.removeLoop(head);
        System.out.println("After removing loop:");
        printList(head);

        // Example 2: Inbuilt (hardcoded example)
        Node headInbuilt = createNode(1);
        Node second = createNode(2);
        Node third = createNode(3);
        Node fourth = createNode(4);
        headInbuilt.next = second;
        second.next = third;
        third.next = fourth;
        fourth.next = second;  // Creating a loop

        System.out.println("Before removing loop (inbuilt list):");
        printList(headInbuilt);
        Solution.removeLoop(headInbuilt);
        System.out.println("After removing loop (inbuilt list):");
        printList(headInbuilt);

        scanner.close();
    }
}
