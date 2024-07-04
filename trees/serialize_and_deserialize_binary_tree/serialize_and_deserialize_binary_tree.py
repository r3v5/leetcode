from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # base case
        if not root:
            return ""

        # run bfs level order traversal to serialize each subtree on each level
        queue = deque([root])
        result = []

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                if not node:
                    result.append("#")

                else:
                    result.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)

        print(",".join(result))
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        # run bfs level order to build tree
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])

        # since we already created root
        i = 1

        while queue:

            node = queue.popleft()

            if values[i] != "#":
                left = TreeNode(int(values[i]))
                node.left = left
                queue.append(node.left)

            i += 1

            if values[i] != "#":
                right = TreeNode(int(values[i]))
                node.right = right
                queue.append(node.right)

            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
