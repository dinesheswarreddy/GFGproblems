//Linked List Group Reverse
import java.util.Scanner;

class Node {
    int data;
    Node next;
    
    // Constructor to create a new node
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Solution {
    public static Node reverseKGroup(Node head, int k) {
        if (head == null) {
            return head;
        }

        Node curr = head;
        Node newHead = null;
        Node tail = null;

        while (curr != null) {
            Node groupHead = curr;
            Node prev = null;
            Node nextNode = null;
            int count = 0;
            while (curr != null && count < k) {
                nextNode = curr.next;
                curr.next = prev;
                prev = curr;
                curr = nextNode;
                count++;
            }

            if (newHead == null) {
                newHead = prev;
            }

            if (tail != null) {
                tail.next = prev;
            }

            tail = groupHead;
        }

        return newHead;
    }

    // Function to print the linked list
    public static void printList(Node head) {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    // Function to create a linked list from an array of integers
    public static Node createList(int[] arr) {
        if (arr.length == 0) return null;
        
        Node head = new Node(arr[0]);
        Node temp = head;
        for (int i = 1; i < arr.length; i++) {
            temp.next = new Node(arr[i]);
            temp = temp.next;
        }
        return head;
    }

    public static void main(String[] args) {
        // Example 1: Hardcoded input (inbuilt)
        int[] inbuiltArr = {1, 2, 3, 4, 5};
        Node inbuiltHead = createList(inbuiltArr);
        int kInbuilt = 3;
        System.out.println("Original list (Inbuilt):");
        printList(inbuiltHead);
        Node reversedInbuiltHead = reverseKGroup(inbuiltHead, kInbuilt);
        System.out.println("Reversed list (Inbuilt) after " + kInbuilt + " groups:");
        printList(reversedInbuiltHead);

        // Example 2: User input
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of elements in the linked list:");
        int n = scanner.nextInt();
        System.out.println("Enter the elements of the linked list:");
        int[] userArr = new int[n];
        for (int i = 0; i < n; i++) {
            userArr[i] = scanner.nextInt();
        }
        System.out.println("Enter the value of k:");
        int kUser = scanner.nextInt();

        Node userHead = createList(userArr);
        System.out.println("Original list (User input):");
        printList(userHead);
        Node reversedUserHead = reverseKGroup(userHead, kUser);
        System.out.println("Reversed list (User input) after " + kUser + " groups:");
        printList(reversedUserHead);

        scanner.close();
    }
}
