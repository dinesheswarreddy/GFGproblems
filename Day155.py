#Implement Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEndOfWord

    def isPrefix(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# ------------------- User Input ----------------------

def run_with_user_input():
    trie = Trie()
    print("Enter number of queries:")
    q = int(input())

    print("Enter queries in format: type word (e.g. 1 abcd)")
    output = []

    for _ in range(q):
        parts = input().split()
        t = int(parts[0])
        word = parts[1]

        if t == 1:
            trie.insert(word)
        elif t == 2:
            output.append(trie.search(word))
        elif t == 3:
            output.append(trie.isPrefix(word))

    print("Results:", output)


# ------------------- Inbuilt Example ----------------------

def run_with_inbuilt_test():
    trie = Trie()
    queries = [
        [1, "abcd"],
        [1, "abc"],
        [1, "bcd"],
        [2, "bc"],
        [3, "bc"],
        [2, "abc"]
    ]

    output = []

    for t, word in queries:
        if t == 1:
            trie.insert(word)
        elif t == 2:
            output.append(trie.search(word))
        elif t == 3:
            output.append(trie.isPrefix(word))

    print("Inbuilt Test Output:", output)


# ------------------- Main ----------------------

if __name__ == "__main__":
    print("Choose input type:\n1. User Input\n2. Inbuilt Test Case")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        run_with_user_input()
    elif choice == "2":
        run_with_inbuilt_test()
    else:
        print("Invalid choice.")
