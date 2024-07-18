from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        hashmap = {}  # old node -> new node
        curr = node

        # run dfs
        stack = [curr]
        visited = set()

        while stack:
            curr = stack.pop()
            hashmap[curr] = Node(val=curr.val)
            visited.add(curr)

            for nei in curr.neighbors:
                if nei not in visited:
                    stack.append(nei)

        # connect edges
        for old_node, new_node in hashmap.items():
            for nei in old_node.neighbors:
                new_nei = hashmap[nei]
                new_node.neighbors.append(new_nei)

        return hashmap[node]

    # Time: O(V + E)
    # Space: O(V)
