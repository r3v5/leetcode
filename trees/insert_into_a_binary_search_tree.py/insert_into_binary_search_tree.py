from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return TreeNode(val)

        node = root

        while node:

            if node.val < val:

                if not node.right:
                    node.right = TreeNode(val)
                    break

                else:
                    node = node.right

            elif node.val > val:

                if not node.left:
                    node.left = TreeNode(val)
                    break

                else:
                    node = node.left

        return root


ex1 = TreeNode(4)
ex1.left = TreeNode(2)
ex1.right = TreeNode(7)
ex1.left.left = TreeNode(1)
ex1.left.right = TreeNode(3)
val = 5
driver = Solution()
print(driver.insertIntoBST(ex1, val))
