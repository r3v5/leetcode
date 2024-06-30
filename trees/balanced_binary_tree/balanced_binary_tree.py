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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # base case
        if not root:
            return True

        # run dfs post-order traversal from the bottom to top to precalculate the heights of children nodes
        stack = [[root, False]]
        heights = {}

        while stack:
            cur, visited = stack.pop()

            if visited:
                left_height = heights.get(cur.left, -1)
                right_height = heights.get(cur.right, -1)

                if abs(left_height - right_height) > 1:
                    return False

                heights[cur] = max(left_height, right_height) + 1

            else:
                stack.append([cur, True])

                if cur.right:
                    stack.append([cur.right, False])

                if cur.left:
                    stack.append([cur.left, False])

        return True


ex1 = TreeNode(3)
ex1.left = TreeNode(9)
ex1.right = TreeNode(20)
ex1.right.left = TreeNode(15)
ex1.right.right = TreeNode(7)

ex2 = TreeNode(1)
ex2.left = TreeNode(2)
ex2.right = TreeNode(2)
ex2.left.left = TreeNode(3)
ex2.left.right = TreeNode(3)
ex2.left.left.left = TreeNode(4)
ex2.left.left.right = TreeNode(4)

ex3 = TreeNode()

driver = Solution()
print(
    f"Example 1:\nInput: root = [3,9,20,null,null,15,7]\nOutput: {driver.isBalanced(ex1)}\n"
)
print(
    f"Example 2:\nInput: root = [1,2,2,3,3,null,null,4,4]\nOutput: {driver.isBalanced(ex2)}\n"
)
print(f"Example 3:\nInput: root = []\nOutput: {driver.isBalanced(ex3)}\n")
