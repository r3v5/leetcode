from typing import Optional


class ListNode:

    # Double Linked List node
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}  # key -> node

        # init left (LRU - Least Recent Used) and right (MRU - Most Recent Used) pointers, dummy nodes
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert_node(self, node: Optional[ListNode]) -> None:
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def delete_node(self, node: Optional[ListNode]) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]

            # delete from list
            self.delete_node(node)

            # insert at the end
            self.insert_node(node)

            return self.hashmap[key].val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]

            # delete from list
            self.delete_node(node)

        node = ListNode(key, value)

        # insert at the end
        self.insert_node(node)

        # add to hashmap
        self.hashmap[key] = node

        # check if exceeded capacity
        if len(self.hashmap) > self.capacity:

            # find LRU
            lru = self.left.next

            # delete LRU
            self.delete_node(self.hashmap[lru.key])
            del self.hashmap[lru.key]

    # Time: O(1)
    # Space: O(n)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Example usage based on the given input and expected output
commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

output = []
lRUCache = None

for i in range(len(commands)):
    command = commands[i]
    args = inputs[i]

    if command == "LRUCache":
        lRUCache = LRUCache(*args)
        output.append(None)
    elif command == "put":
        lRUCache.put(*args)
        output.append(None)
    elif command == "get":
        output.append(lRUCache.get(*args))

print("Expected Output:", [None, None, None, 1, None, -1, None, -1, 3, 4])
print("Output:", output)
