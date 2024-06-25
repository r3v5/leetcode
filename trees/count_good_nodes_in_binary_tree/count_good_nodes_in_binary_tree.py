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
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None

        good_nodes = 0
        stack = [[root, root.val]]

        while stack:
            node, max_val = stack.pop()

            if node.val >= max_val:
                good_nodes += 1

            if node.right:
                stack.append([node.right, max(max_val, node.val)])

            if node.left:
                stack.append([node.left, max(max_val, node.val)])

        return good_nodes


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

driver = Solution()
test_case = driver.goodNodes(root)
print(test_case)
