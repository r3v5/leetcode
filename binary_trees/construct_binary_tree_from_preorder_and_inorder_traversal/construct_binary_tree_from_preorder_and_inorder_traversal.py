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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1) pre-order: (3), (9), (20), (15), (7)
        #               root
        # first node in pre-order list always be the root

        # 2) in-order: (9), (3), (15), (20), (7)
        # left subtree     |root| right subtree

        # base case
        if not preorder or not inorder:
            return None

        # create a root based on preorder first node
        root = TreeNode(preorder[0])

        # find the index of root in inorder list
        inorder_root_index = inorder.index(preorder[0])

        # build left subtree: preorder[1 : inorder_root_index + 1], inorder[:inorder_root_index]
        root.left = self.buildTree(
            preorder[1 : inorder_root_index + 1], inorder[:inorder_root_index]
        )

        # build right subtree preorder[inorder_root_index + 1:], inorder[inorder_root_index + 1:]
        root.right = self.buildTree(
            preorder[inorder_root_index + 1 :], inorder[inorder_root_index + 1 :]
        )

        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
driver = Solution()
print(driver.buildTree(preorder, inorder))
