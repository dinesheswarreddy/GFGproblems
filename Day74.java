//LRU Cache
import java.util.*;
import java.util.Scanner;

class LRUCache {
    private int capacity;
    private Map<Integer, Node> cache;  // HashMap to store key-value pairs
    private DoublyLinkedList dll;  // Doubly Linked List to maintain the LRU order

    // Doubly Linked List Node
    private class Node {
        int key;
        int value;
        Node prev, next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    // Doubly Linked List to manage the order of usage
    private class DoublyLinkedList {
        Node head, tail;

        DoublyLinkedList() {
            head = new Node(0, 0);  // dummy node
            tail = new Node(0, 0);  // dummy node
            head.next = tail;
            tail.prev = head;
        }

        // Add a node right before the tail (most recently used)
        void addLast(Node node) {
            Node prevTail = tail.prev;
            prevTail.next = node;
            node.prev = prevTail;
            node.next = tail;
            tail.prev = node;
        }

        // Remove a node from the list
        void remove(Node node) {
            Node prevNode = node.prev;
            Node nextNode = node.next;
            prevNode.next = nextNode;
            nextNode.prev = prevNode;
        }

        // Remove the first node (least recently used)
        Node removeFirst() {
            if (head.next == tail) return null;  // List is empty
            Node first = head.next;
            remove(first);
            return first;
        }
    }

    // Constructor to initialize the cache with a given capacity
    public LRUCache(int cap) {
        capacity = cap;
        cache = new HashMap<>();
        dll = new DoublyLinkedList();
    }

    // Function to return the value corresponding to the key.
    public int get(int key) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            dll.remove(node);
            dll.addLast(node);  // Move the accessed node to the tail (most recently used)
            return node.value;
        }
        return -1;  // Key not found
    }

    // Function for storing key-value pair.
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            // Update the value and move the node to the tail (most recently used)
            Node node = cache.get(key);
            node.value = value;
            dll.remove(node);
            dll.addLast(node);
        } else {
            // If the cache is full, remove the least recently used item
            if (cache.size() == capacity) {
                Node leastRecentlyUsed = dll.removeFirst();
                cache.remove(leastRecentlyUsed.key);  // Remove from the cache map
            }
            // Create a new node and add it to the cache
            Node newNode = new Node(key, value);
            dll.addLast(newNode);
            cache.put(key, newNode);
        }
    }
}

public class LRUCacheExample {
    public static void main(String[] args) {
        // Inbuilt Example Usage
        System.out.println("Inbuilt Example:");
        LRUCache cache = new LRUCache(2);
        cache.put(1, 2);
        cache.put(2, 3);
        System.out.println(cache.get(1)); // Expected: 2
        cache.put(1, 5);
        System.out.println(cache.get(1)); // Expected: 5
        System.out.println(cache.get(4)); // Expected: -1

        // User Input Example Usage
        Scanner sc = new Scanner(System.in);
        System.out.println("\nEnter the capacity of the cache:");
        int capacity = sc.nextInt();
        System.out.println("Enter the number of queries:");
        int queries = sc.nextInt();
        LRUCache userCache = new LRUCache(capacity);
        
        sc.nextLine();  // To consume the newline character

        for (int i = 0; i < queries; i++) {
            System.out.println("Enter query (PUT x y or GET x):");
            String query = sc.nextLine();
            String[] queryParts = query.split(" ");
            
            if (queryParts[0].equals("PUT")) {
                int key = Integer.parseInt(queryParts[1]);
                int value = Integer.parseInt(queryParts[2]);
                userCache.put(key, value);
                System.out.println("PUT " + key + " " + value + " executed.");
            } else if (queryParts[0].equals("GET")) {
                int key = Integer.parseInt(queryParts[1]);
                int result = userCache.get(key);
                System.out.println("GET " + key + " result: " + result);
            }
        }
        
        sc.close();
    }
}
