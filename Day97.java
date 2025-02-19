#Merge K sorted linked lists
import java.util.*;

class Node {
    int data;
    Node next;

    Node(int key) {
        data = key;
        next = null;
    }
}

class Solution {
    // Function to merge K sorted linked lists.
    Node mergeKLists(List<Node> arr) {
        // Priority queue to store the nodes, with the node value as the key for sorting.
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.data - b.data);
        
        // Step 1: Insert the first node from each list into the priority queue.
        for (Node head : arr) {
            if (head != null) {
                pq.add(head);
            }
        }

        // Step 2: Create a dummy node for the result list and a pointer to build the result.
        Node dummy = new Node(0);
        Node current = dummy;

        // Step 3: Pop the smallest node from the heap, add it to the result list, and if it has a next, add that to the heap.
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            current.next = node;  // Add the node to the result list
            current = current.next;  // Move the current pointer forward
            
            if (node.next != null) {
                pq.add(node.next);  // If the node has a next, push it into the heap
            }
        }

        // Step 4: Return the head of the merged list.
        return dummy.next;
    }

    // Utility function to print the linked list
    void printList(Node head) {
        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Inbuilt Example: Merging 3 sorted lists
        List<Node> lists = new ArrayList<>();
        
        // First list: 1 -> 4 -> 5
        Node list1 = new Node(1);
        list1.next = new Node(4);
        list1.next.next = new Node(5);
        lists.add(list1);

        // Second list: 1 -> 3 -> 4
        Node list2 = new Node(1);
        list2.next = new Node(3);
        list2.next.next = new Node(4);
        lists.add(list2);

        // Third list: 2 -> 6
        Node list3 = new Node(2);
        list3.next = new Node(6);
        lists.add(list3);

        // Merging the lists
        Node mergedList = sol.mergeKLists(lists);
        System.out.print("Merged List (Inbuilt Example): ");
        sol.printList(mergedList);  // Expected output: 1 1 2 3 4 4 5 6

        // User input example:
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter number of lists: ");
        int n = scanner.nextInt();

        List<Node> userLists = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            System.out.println("Enter the number of elements in list " + (i + 1) + ": ");
            int m = scanner.nextInt();
            Node head = null, current = null;
            System.out.println("Enter the elements of the list: ");
            for (int j = 0; j < m; j++) {
                int value = scanner.nextInt();
                Node newNode = new Node(value);
                if (head == null) {
                    head = newNode;
                    current = head;
                } else {
                    current.next = newNode;
                    current = current.next;
                }
            }
            userLists.add(head);
        }

        Node mergedUserList = sol.mergeKLists(userLists);
        System.out.print("Merged List (User Input): ");
        sol.printList(mergedUserList);  // Output will depend on user input
    }
}
