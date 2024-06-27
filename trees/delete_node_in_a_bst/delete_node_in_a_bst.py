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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return root

        # finding the node to delete
        cur = root

        if key > cur.val:
            cur.right = self.deleteNode(cur.right, key)
        elif key < cur.val:
            cur.left = self.deleteNode(cur.left, key)
        else:

            # check if there is only one child
            if not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left

            # if there are two children -> find the min node from right subtree and change the min node with node to delete
            # after delete the the min node from right subtree because now it's a parent node instead of node to delete
            min_node = self.find_min_node_in_bst(cur.right)
            cur.val = min_node.val
            cur.right = self.deleteNode(cur.right, min_node.val)

        return cur

    def find_min_node_in_bst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        cur = root

        while cur.left:
            cur = cur.left

        return cur


ex1 = TreeNode(5)
ex1.left = TreeNode(3)
ex1.right = TreeNode(6)
ex1.left.left = TreeNode(2)
ex1.left.right = TreeNode(4)
ex1.right = TreeNode(6)
ex1.right.right = TreeNode(7)
key = 3
driver = Solution()
print(driver.deleteNode(ex1, key))
