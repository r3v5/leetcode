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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0

        # since root is the fist
        prev_level = 1
        leftmost_index = 1

        # queue -> node, index, level
        queue = deque([[root, 1, 1]])

        while queue:
            node, index, level = queue.popleft()

            if level > prev_level:
                prev_level = level
                leftmost_index = index

            max_width = max(max_width, index - leftmost_index + 1)

            if node.left:
                queue.append([node.left, 2 * index, level + 1])

            if node.right:
                queue.append([node.right, 2 * index + 1, level + 1])

        return max_width


ex1 = TreeNode(1)
ex1.left = TreeNode(3)
ex1.right = TreeNode(2)
ex1.left.left = TreeNode(5)
ex1.left.right = TreeNode(3)
ex1.right = TreeNode(2)
ex1.right.right = TreeNode(9)

ex2 = TreeNode(1)
ex2.left = TreeNode(3)
ex2.right = TreeNode(2)
ex2.left.left = TreeNode(5)
ex2.left.left.left = TreeNode(6)
ex2.right.right = TreeNode(9)
ex2.right.right.left = TreeNode(7)

ex3 = TreeNode(1)
ex3.left = TreeNode(3)
ex3.right = TreeNode(2)
ex3.left.left = TreeNode(5)

driver = Solution()
print(
    f"Example 1:\nInput: root = [1,3,2,5,3,null,9]\nOutput: {driver.widthOfBinaryTree(ex1)}\n"
)
print(
    f"Example 2:\nInput: root = [1,3,2,5,null,null,9,6,null,7]\nOutput: {driver.widthOfBinaryTree(ex2)}\n"
)
print(f"Example 3:\nInput: root = [1,3,2,5]\nOutput: {driver.widthOfBinaryTree(ex3)}")
