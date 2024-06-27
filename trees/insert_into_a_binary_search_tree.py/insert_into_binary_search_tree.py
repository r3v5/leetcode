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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if not root:
            return new_node

        cur = root

        while cur:

            if cur.val < val:

                if not cur.right:
                    cur.right = new_node
                    break

                else:
                    cur = cur.right

            else:

                if not cur.left:
                    cur.left = new_node
                    break

                else:
                    cur = cur.left

        return root


ex1 = TreeNode(4)
ex1.left = TreeNode(2)
ex1.right = TreeNode(7)
ex1.left.left = TreeNode(1)
ex1.left.right = TreeNode(3)
val = 5
driver = Solution()
print(driver.insertIntoBST(ex1, val))
