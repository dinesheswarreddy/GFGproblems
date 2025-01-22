//Add Number Linked Lists
#include <iostream>
using namespace std;

// Definition for singly-linked list
class Node {
public:
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class Solution {
public:
    // Function to reverse a linked list
    Node* reverse(Node* head) {
        Node* prev = nullptr;
        Node* curr = head;
        Node* next;
        while (curr != nullptr) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    // Function to trim leading zeros
    Node* trimLeadingZeros(Node* head) {
        while (head != nullptr && head->data == 0) {
            head = head->next;
        }
        return head;
    }

    // Function to count the number of nodes in the linked list
    int countNodes(Node* head) {
        int len = 0;
        Node* curr = head;
        while (curr != nullptr) {
            len += 1;
            curr = curr->next;
        }
        return len;
    }

    // Function to add two linked lists
    Node* addTwoLists(Node* num1, Node* num2) {
        // Trim leading zeros from both lists
        num1 = trimLeadingZeros(num1);
        num2 = trimLeadingZeros(num2);

        // Reverse both lists to make the addition easier
        num1 = reverse(num1);
        num2 = reverse(num2);

        Node* res = nullptr;  // Result list
        Node* temp = nullptr; // Temporary pointer to build the result list
        int carry = 0;

        // Traverse both lists and add the numbers
        while (num1 != nullptr || num2 != nullptr || carry != 0) {
            int sum = carry;
            if (num1 != nullptr) {
                sum += num1->data;
                num1 = num1->next;
            }
            if (num2 != nullptr) {
                sum += num2->data;
                num2 = num2->next;
            }

            carry = sum / 10;
            sum = sum % 10;

            // Create a new node with the sum and add it to the result list
            Node* newNode = new Node(sum);
            if (res == nullptr) {
                res = newNode;  // First node in the result list
            } else {
                temp->next = newNode;
            }
            temp = newNode;
        }

        // Reverse the result list to get the correct order
        return reverse(res);
    }

    // Function to print the linked list
    void printList(Node* head) {
        if (head == nullptr) {
            cout << "Empty List" << endl;
            return;
        }
        while (head != nullptr) {
            cout << head->data;
            if (head->next != nullptr) {
                cout << " -> ";
            }
            head = head->next;
        }
        cout << endl;
    }

    // Function to create a linked list from an array of integers
    Node* buildList(int arr[], int size) {
        if (size == 0) return nullptr;
        Node* head = new Node(arr[0]);
        Node* temp = head;
        for (int i = 1; i < size; ++i) {
            temp->next = new Node(arr[i]);
            temp = temp->next;
        }
        return head;
    }
};

int main() {
    Solution solution;

    // Example 1: In-built input
    int arr1[] = {2, 4, 3};  // Linked list for 342
    int arr2[] = {5, 6, 4};  // Linked list for 465
    Node* num1 = solution.buildList(arr1, 3);
    Node* num2 = solution.buildList(arr2, 3);

    cout << "In-built input (num1): ";
    solution.printList(num1);
    cout << "In-built input (num2): ";
    solution.printList(num2);

    Node* result = solution.addTwoLists(num1, num2);
    cout << "Result of addition: ";
    solution.printList(result);

    // Example 2: User input
    cout << "Enter the number of elements in the first list: ";
    int n1;
    cin >> n1;
    cout << "Enter the elements for the first list: ";
    int* userArr1 = new int[n1];
    for (int i = 0; i < n1; ++i) {
        cin >> userArr1[i];
    }

    cout << "Enter the number of elements in the second list: ";
    int n2;
    cin >> n2;
    cout << "Enter the elements for the second list: ";
    int* userArr2 = new int[n2];
    for (int i = 0; i < n2; ++i) {
        cin >> userArr2[i];
    }

    Node* userNum1 = solution.buildList(userArr1, n1);
    Node* userNum2 = solution.buildList(userArr2, n2);

    cout << "User input (num1): ";
    solution.printList(userNum1);
    cout << "User input (num2): ";
    solution.printList(userNum2);

    Node* userResult = solution.addTwoLists(userNum1, userNum2);
    cout << "Result of addition: ";
    solution.printList(userResult);

    delete[] userArr1;
    delete[] userArr2;

    return 0;
}
