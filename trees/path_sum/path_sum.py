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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        if not root:
            return False

        # run dfs pre-order
        stack = [[root, root.val]]

        while stack:
            node, cur_sum = stack.pop()

            # check if reached a leaf
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    return True

            if node.right:
                stack.append([node.right, cur_sum + node.right.val])

            if node.left:
                stack.append([node.left, cur_sum + node.left.val])

        return False


ex1 = TreeNode(5)
ex1.left = TreeNode(4)
ex1.right = TreeNode(8)
ex1.left.left = TreeNode(11)
ex1.left.left.left = TreeNode(7)
ex1.left.left.right = TreeNode(2)
ex1.right.left = TreeNode(13)
ex1.right.right = TreeNode(4)
ex1.right.right.right = TreeNode(1)
targetSum1 = 22

ex2 = TreeNode(1)
ex2.left = TreeNode(2)
ex2.right = TreeNode(3)
targetSum2 = 5

driver = Solution()

print(
    f"Example 1:\nInput: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22\nOutput: {driver.hasPathSum(ex1, targetSum1)}\n"
)
print(
    f"Example 2:\nInput: root = [1,2,3], targetSum = 5\nOutput: {driver.hasPathSum(ex2, targetSum2)}"
)
