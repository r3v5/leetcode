class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # start from the root
        curr = self.root

        # go through the word char by char
        for char in word:

            # add new TrieNode by char to children hashmap if it doesn't exist there
            if char not in curr.children:
                curr.children[char] = TrieNode()

            # move to next node
            curr = curr.children[char]

        # mark last node like the end of the word
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return True

    # Time: O(n) n is the length of the string used in the operation.
    # Space: O(n)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie()

# Perform the operations
operations = ["insert", "search", "search", "startsWith", "insert", "search"]
arguments = [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

# Expected output
expected_output = [None, True, False, True, None, True]

# Store actual output
actual_output = []

for i in range(len(operations)):
    if operations[i] == "insert":
        trie.insert(arguments[i][0])
        actual_output.append(None)
    elif operations[i] == "search":
        result = trie.search(arguments[i][0])
        actual_output.append(result)
    elif operations[i] == "startsWith":
        result = trie.startsWith(arguments[i][0])
        actual_output.append(result)

print("Actual Output:", actual_output)
print("Expected Output:", expected_output)

# Check if actual output matches expected output
print("Test Passed:", actual_output == expected_output)
