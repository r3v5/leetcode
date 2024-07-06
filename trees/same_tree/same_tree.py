from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases
        if not p and not q:
            return True

        if not p or not q:
            return False

        # run dfs pre-order
        stack = [[p, q]]

        while stack:
            tree_node_1, tree_node_2 = stack.pop()

            if not tree_node_1 and not tree_node_2:
                continue

            if not tree_node_1 or not tree_node_2:
                return False

            if tree_node_1.val != tree_node_2.val:
                return False

            stack.append([tree_node_1.right, tree_node_2.right])
            stack.append([tree_node_1.left, tree_node_2.left])

        return True
