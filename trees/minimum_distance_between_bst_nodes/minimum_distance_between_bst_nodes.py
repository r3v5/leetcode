from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0

        # run dfs pre-order traversal
        stack = [[root, float("-inf"), float("inf")]]
        min_diff = float("inf")

        while stack:
            node, lower_val, bigger_val = stack.pop()

            # check difference between lower node value
            min_diff = min(min_diff, node.val - lower_val)

            # check difference between bigger node value
            min_diff = min(min_diff, bigger_val - node.val)

            if node.right:
                stack.append([node.right, node.val, bigger_val])

            if node.left:
                stack.append([node.left, lower_val, node.val])

        return min_diff


ex1 = TreeNode(4)
ex1.left = TreeNode(2)
ex1.right = TreeNode(6)
ex1.left.left = TreeNode(1)
ex1.left.right = TreeNode(3)

ex2 = TreeNode(1)
ex2.left = TreeNode(0)
ex2.right = TreeNode(48)
ex2.right.left = TreeNode(12)
ex2.right.right = TreeNode(49)

driver = Solution()
print(f"Example 1:\nInput: root = [4,2,6,1,3]\nOutput: {driver.minDiffInBST(ex1)}\n")
print(
    f"Example 2:\nInput: root = [1,0,48,null,null,12,49]\nOutput: {driver.minDiffInBST(ex2)}\n"
)
