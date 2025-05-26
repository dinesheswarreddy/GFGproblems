//Insert in Sorted Circular Linked List

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
    public Node sortedInsert(Node head, int data) {
        Node newNode = new Node(data);

        // Case 1: Empty list
        if (head == null) {
            newNode.next = newNode;
            return newNode;
        }

        Node current = head;

        while (true) {
            // Case 2: Normal insert between two nodes
            if (current.data <= data && data <= current.next.data) {
                break;
            }

            // Case 3: At the rotation point (max -> min)
            if (current.data > current.next.data) {
                if (data >= current.data || data <= current.next.data) {
                    break;
                }
            }

            current = current.next;

            // Case 4: Completed full loop
            if (current == head) {
                break;
            }
        }

        // Insert new node
        newNode.next = current.next;
        current.next = newNode;

        // Update head if new node is the smallest
        if (data < head.data) {
            return newNode;
        }

        return head;
    }

    // Method to print the circular linked list
    public void printList(Node head) {
        if (head == null) return;

        Node temp = head;
        do {
            System.out.print(temp.data + " ");
            temp = temp.next;
        } while (temp != head);
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        // === User input ===
        System.out.println("Enter number of nodes:");
        int n = sc.nextInt();

        if (n < 1) {
            System.out.println("List is empty.");
            return;
        }

        System.out.println("Enter " + n + " sorted values:");
        int val = sc.nextInt();
        Node head = new Node(val);
        Node tail = head;

        for (int i = 1; i < n; i++) {
            val = sc.nextInt();
            Node temp = new Node(val);
            tail.next = temp;
            tail = temp;
        }
        // Make it circular
        tail.next = head;

        System.out.println("Enter value to insert:");
        int insertData = sc.nextInt();

        head = sol.sortedInsert(head, insertData);

        System.out.println("Updated Circular Linked List:");
        sol.printList(head);

        // === Inbuilt example ===
        System.out.println("\nRunning inbuilt example...");
        Node h = new Node(1);
        h.next = new Node(4);
        h.next.next = new Node(7);
        h.next.next.next = new Node(9);
        h.next.next.next.next = h; // circular

        Node newHead = sol.sortedInsert(h, 5);
        System.out.println("Inbuilt Example Output:");
        sol.printList(newHead);
    }
}
