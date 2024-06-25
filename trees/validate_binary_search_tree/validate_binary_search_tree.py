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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # run dfs preorder traversal
        min_val = float("-inf")
        max_val = float("inf")
        stack = [[root, min_val, max_val]]

        while stack:
            node, min_val, max_val = stack.pop()

            if not node:
                continue

            if not (min_val < node.val < max_val):
                return False

            if node.right:
                stack.append([node.right, node.val, max_val])

            if node.left:
                stack.append([node.left, min_val, node.val])

        return True


ex1_root = TreeNode(2)
ex1_root.left = TreeNode(1)
ex1_root.right = TreeNode(3)

ex1_driver = Solution()
ex1 = ex1_driver.isValidBST(ex1_root)
print(ex1)


ex2_root = TreeNode(5)
ex2_root.left = TreeNode(1)
ex2_root.right = TreeNode(4)
ex2_root.right.left = TreeNode(3)
ex2_root.right.right = TreeNode(6)

ex2_driver = Solution()
ex2 = ex2_driver.isValidBST(ex2_root)
print(ex2)
