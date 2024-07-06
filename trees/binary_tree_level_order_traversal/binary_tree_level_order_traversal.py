from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case
        if not root:
            return None

        # run bfs level order traversal
        queue = deque([root])
        result = []

        while queue:
            level_length = len(queue)
            nodes = []

            for i in range(level_length):
                node = queue.popleft()
                nodes.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(nodes)

        return result
