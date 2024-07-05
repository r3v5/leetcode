from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # dfs postorder: left -> right -> parent
        if not root:
            return None

        result = []
        stack = [[root, False]]

        while stack:
            cur, visited = stack.pop()

            if visited:
                result.append(cur.val)

            else:
                stack.append([cur, True])

                if cur.right:
                    stack.append([cur.right, False])

                if cur.left:
                    stack.append([cur.left, False])

        return result
