from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # base case
        if not head:
            return None

        # populate hashmap by copies of nodes
        old_to_new = {}
        node = head

        while node:
            copy_node = Node(node.val)
            old_to_new[node] = copy_node
            node = node.next

        # assign next and random pointers
        node = head
        while node:
            copy_node = old_to_new[node]

            if node.next:
                copy_node.next = old_to_new[node.next]

            else:
                copy_node.next = None

            if node.random:
                copy_node.random = old_to_new[node.random]

            else:
                copy_node.random = None

            node = node.next

        return old_to_new[head]

    # Time: O(n)
    # Space: O(n)


# Helper function to print the list for verification
def print_list(head: "Optional[Node]"):
    nodes = []
    while head:
        random_val = head.random.val if head.random else None
        nodes.append(f"[{head.val}, {random_val}]")
        head = head.next
    return " -> ".join(nodes)


# Create example list
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

# Solution instance
solution = Solution()

# Deep copy the list
copied_head = solution.copyRandomList(node1)

# Print original and copied lists
print("Original list:", print_list(node1))
print("Copied list:", print_list(copied_head))
