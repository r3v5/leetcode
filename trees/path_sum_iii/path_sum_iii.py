from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: int = None, right: int = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # base case
        if not root:
            return 0

        # run dfs pre-order from up to bottom
        result = 0
        path = [root.val]
        stack = [[root, path]]

        while stack:
            node, path = stack.pop()

            # iterate through each sub-path and check if sum == targetSum
            cur_sum = 0
            for val in path[::-1]:
                cur_sum += val
                if cur_sum == targetSum:
                    result += 1

            if node.right:
                stack.append([node.right, path + [node.right.val]])

            if node.left:
                stack.append([node.left, path + [node.left.val]])

        return result


ex1 = TreeNode(10)
ex1.left = TreeNode(5)
ex1.right = TreeNode(-3)
ex1.left.left = TreeNode(3)
ex1.left.right = TreeNode(2)
ex1.left.left.left = TreeNode(3)
ex1.left.left.right = TreeNode(-2)
ex1.left.right.right = TreeNode(1)
ex1.right.right = TreeNode(11)
target_sum_1 = 8

ex2 = TreeNode(5)
ex2.left = TreeNode(4)
ex2.right = TreeNode(8)
ex2.left.left = TreeNode(11)
ex2.left.left.left = TreeNode(7)
ex2.left.left.right = TreeNode(2)
ex2.right.left = TreeNode(13)
ex2.right.right = TreeNode(4)
ex2.right.right.left = TreeNode(5)
ex2.right.right.right = TreeNode(1)
target_sum_2 = 22

driver = Solution()
print(
    f"Example 1:\nInput: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8\nOutput: {driver.pathSum(ex1, target_sum_1)}\n"
)
print(
    f"Example 2:\nInput: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22\nOutput: {driver.pathSum(ex2, target_sum_2)}"
)
