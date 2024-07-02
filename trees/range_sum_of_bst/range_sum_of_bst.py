from collections import deque
from typing import Optional


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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # run bfs level order
        result = 0
        queue = deque([root])

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                if low <= node.val <= high:
                    result += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result


ex1 = TreeNode(10)
ex1.left = TreeNode(5)
ex1.right = TreeNode(15)
ex1.left.left = TreeNode(3)
ex1.left.right = TreeNode(7)
ex1.right.right = TreeNode(18)
ex1_low = 7
ex1_high = 15

ex2 = TreeNode(10)
ex2.left = TreeNode(5)
ex2.right = TreeNode(15)
ex2.left.left = TreeNode(3)
ex2.left.right = TreeNode(7)
ex2.left.left.left = TreeNode(1)
ex2.left.right.left = TreeNode(6)
ex2.right.left = TreeNode(13)
ex2.right.right = TreeNode(18)
ex2_low = 6
ex2_high = 10

driver = Solution()
print(
    f"Example 1:\nInput: root = [10,5,15,3,7,null,18], low = 7, high = 15\nOutput: {driver.rangeSumBST(ex1, ex1_low, ex1_high)}\n"
)
print(
    f"Example 2:\nInput: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10\nOutput: {driver.rangeSumBST(ex2, ex2_low, ex2_high)}\n"
)
