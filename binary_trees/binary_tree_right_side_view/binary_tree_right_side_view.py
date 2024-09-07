from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # base cases
        if not root:
            return None

        # bfs level order traversal only getting right nodes
        queue = deque([root])
        res = []

        while queue:
            level_length = len(queue)
            rigthmost_node = None

            for i in range(level_length):
                node = queue.popleft()
                if node:
                    rigthmost_node = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if rigthmost_node:
                res.append(rigthmost_node.val)

        return res


driver = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
test_case = driver.rightSideView(root)
print(test_case)
