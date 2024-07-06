from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base cases
        if not root:
            return False

        if not subRoot:
            return True

        # run dfs pre-order
        stack = [root]

        while stack:
            node = stack.pop()

            if self.is_same_tree(node, subRoot):
                return True

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return False

    def is_same_tree(
        self, tree_1: Optional[TreeNode], tree_2: Optional[TreeNode]
    ) -> bool:
        # base cases
        if not tree_1:
            return False

        if not tree_2:
            return True

        # run dfs pre-order
        stack = [[tree_1, tree_2]]

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
