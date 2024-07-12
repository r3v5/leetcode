from collections import deque
from typing import Optional


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

    def largest_smaller_bst_key(self, root: Optional[TreeNode], val: int) -> int:
        # bfs
        queue = deque([root])
        result = float("-inf")

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                if node.val < val:
                    result = max(result, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result


root = TreeNode(20)
root.left = TreeNode(9)
root.right = TreeNode(25)
root.left.left = TreeNode(5)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(11)
root.left.right.right = TreeNode(14)
val = 17

driver = Solution()

print(f"Result: {driver.largest_smaller_bst_key(root, val)}")
