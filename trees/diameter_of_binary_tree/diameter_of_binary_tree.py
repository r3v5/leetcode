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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # use dfs for traversing the bst and calculating the height of each node ones and the max diameter

        if root == None:
            return -1

        diameter = 0
        stack = [[root, False]]
        height = {}

        while stack:
            cur, visited = stack.pop()

            if visited:
                left_height = height.get(cur.left, -1)
                right_height = height.get(cur.right, -1)
                height[cur] = 1 + max(left_height, right_height)
                diameter = max(diameter, 2 + left_height + right_height)

            else:
                stack.append([cur, True])

                if cur.right:
                    stack.append([cur.right, False])

                if cur.left:
                    stack.append([cur.left, False])

        return diameter


ex1 = TreeNode(1)
ex1.left = TreeNode(2)
ex1.right = TreeNode(3)
ex1.left.left = TreeNode(4)
ex1.left.right = TreeNode(5)

ex2 = TreeNode(1)
ex2.left = TreeNode(2)

driver = Solution()
print(driver.diameterOfBinaryTree(ex1))
print(driver.diameterOfBinaryTree(ex2))
