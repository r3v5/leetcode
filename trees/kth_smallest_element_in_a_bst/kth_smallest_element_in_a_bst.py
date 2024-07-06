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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs in-order from top to bottom
        stack = []
        node = root
        count_smallest = 0

        while stack or node:

            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            count_smallest += 1

            if count_smallest == k:
                return node.val

            node = node.right

        return None


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
k = 3

driver = Solution()
print(driver.kthSmallest(root, k))


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
k = 1

driver = Solution()
print(driver.kthSmallest(root, k))
