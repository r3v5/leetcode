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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        # run bfs using queue
        queue = deque([root])
        level = 0
        result = []

        while queue:
            level_length = len(queue)
            nodes = []

            for i in range(level_length):
                node = queue.popleft()

                if not node:
                    continue

                nodes.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

            if level % 2 == 0:
                result.append(nodes[::-1])
            else:
                result.append(nodes)

        return result


ex1 = TreeNode(3)
ex1.left = TreeNode(9)
ex1.right = TreeNode(20)
ex1.right.left = TreeNode(15)
ex1.right.right = TreeNode(7)

ex2 = TreeNode(1)

driver = Solution()
print(
    f"Example 1:\nInput: root = [3,9,20,null,null,15,7]\nOutput: {driver.zigzagLevelOrder(ex1)}\n"
)
print(f"Example 2:\nInput: root = [1]\nOutput: {driver.zigzagLevelOrder(ex2)}")
