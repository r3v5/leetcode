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
    def maxPathSum(self, root: TreeNode) -> int:
        # base case
        if not root:
            return 0

        # run dfs post-order to precalculate sum of paths of ancestor's children
        stack = [[root, False]]
        max_path = float("-inf")

        # hashmap for storing sum of path by current node
        paths = {}

        while stack:
            node, visited = stack.pop()

            if visited:
                # avoid negative nodes
                left_path_sum = max(paths.get(node.left, 0), 0)
                right_path_sum = max(paths.get(node.right, 0), 0)

                max_path = max(max_path, left_path_sum + node.val + right_path_sum)

                paths[node] = node.val + max(left_path_sum, right_path_sum)

            else:
                stack.append([node, True])

                if node.right:
                    stack.append([node.right, False])

                if node.left:
                    stack.append([node.left, False])

        return max_path


ex1 = TreeNode(1)
ex1.left = TreeNode(2)
ex1.right = TreeNode(3)

ex2 = TreeNode(-10)
ex2.left = TreeNode(9)
ex2.right = TreeNode(20)
ex2.right.left = TreeNode(15)
ex2.right.right = TreeNode(7)

driver = Solution()

print(f"Example 1:\nInput: root = [1,2,3]\nOutput: {driver.maxPathSum(ex1)}\n")
print(
    f"Example 2:\nInput: root = [-10,9,20,null,null,15,7]\nOutput: {driver.maxPathSum(ex2)}\n"
)
