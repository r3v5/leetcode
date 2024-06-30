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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # base case
        if not root:
            return None

        # dfs pre-order
        cur_sum = root.val
        path = [root.val]
        stack = [[root, path, cur_sum]]
        result = []

        while stack:
            cur, path, cur_sum = stack.pop()

            # check if we reached a leaf node and current sum equals to targetSum
            if not cur.left and not cur.right and cur_sum == targetSum:
                result.append(path)

            if cur.right:
                stack.append(
                    [cur.right, path + [cur.right.val], cur_sum + cur.right.val]
                )

            if cur.left:
                stack.append([cur.left, path + [cur.left.val], cur_sum + cur.left.val])

        return result


ex1 = TreeNode(5)
ex1.left = TreeNode(4)
ex1.right = TreeNode(8)
ex1.left.left = TreeNode(11)
ex1.left.left.left = TreeNode(7)
ex1.left.left.right = TreeNode(2)
ex1.right.left = TreeNode(13)
ex1.right.right = TreeNode(4)
ex1.right.right.left = TreeNode(5)
ex1.right.right.right = TreeNode(1)
targetSum = 22

ex2 = TreeNode(1)
ex2.left = TreeNode(2)
ex2.right = TreeNode(3)


driver = Solution()
print(
    f"Example 1:\nInput: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22\nOutput: {driver.pathSum(ex1, targetSum)}\n"
)
print(
    f"Example 2:\nInput: root = [1, 2, 3], targetSum = 5\nOutput: {driver.pathSum(ex2, 5)}"
)
