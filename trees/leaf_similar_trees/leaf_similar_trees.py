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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        left_tree_leaves_seq = self.get_leaves_sequence(root1)
        right_tree_leaves_seq = self.get_leaves_sequence(root2)

        return left_tree_leaves_seq == right_tree_leaves_seq

    def get_leaves_sequence(self, root: Optional[TreeNode]) -> Optional[List]:
        # run dfs post-order traversal for bottom to up to get all leaves at the beginning
        leaves = []
        stack = [[root, False]]

        while stack:
            node, visited = stack.pop()

            if visited:

                # check if we reached leaf node in tree
                if not node.left and not node.right:
                    leaves.append(node.val)

            else:
                stack.append([node, True])

                if node.right:
                    stack.append([node.right, False])

                if node.left:
                    stack.append([node.left, False])

        return leaves


# Example usage
ex1_root1 = TreeNode(3)
ex1_root1.left = TreeNode(5)
ex1_root1.right = TreeNode(1)
ex1_root1.left.left = TreeNode(6)
ex1_root1.left.right = TreeNode(2)
ex1_root1.left.right.left = TreeNode(7)
ex1_root1.left.right.right = TreeNode(4)
ex1_root1.right.left = TreeNode(9)
ex1_root1.right.right = TreeNode(8)

ex1_root2 = TreeNode(3)
ex1_root2.left = TreeNode(5)
ex1_root2.right = TreeNode(1)
ex1_root2.left.left = TreeNode(6)
ex1_root2.left.right = TreeNode(7)
ex1_root2.right.left = TreeNode(4)
ex1_root2.right.right = TreeNode(2)
ex1_root2.right.right.left = TreeNode(9)
ex1_root2.right.right.right = TreeNode(8)

driver = Solution()

print(driver.get_leaves_sequence(ex1_root1))
print(driver.get_leaves_sequence(ex1_root2))

print(
    f"Example 1:\nInput: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]\nOutput: {driver.leafSimilar(ex1_root1, ex1_root2)}\n"
)
