from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # dfs pre-order: parent -> left -> right
        if not root:
            return None

        result = []
        stack = [root]

        while stack:
            cur = stack.pop()
            result.append(cur.val)

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)

        return result
