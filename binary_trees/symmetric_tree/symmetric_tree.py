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


# Iterative DFS Pre-order solution
class IterativeSolution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [[root.left, root.right]]

        while stack:
            left_subtree, right_subtree = stack.pop()

            if not left_subtree and not right_subtree:
                continue

            if not left_subtree or not right_subtree:
                return False

            if left_subtree.val != right_subtree.val:
                return False

            stack.append([left_subtree.right, right_subtree.left])
            stack.append([left_subtree.left, right_subtree.right])

        return True


# Recursive DFS Pre-order solution
class RecursiveSolution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(
        self, left_subtree: Optional[TreeNode], right_subtree: Optional[TreeNode]
    ) -> bool:
        if not left_subtree and not right_subtree:
            return True

        if not left_subtree or not right_subtree:
            return False

        if left_subtree.val != right_subtree.val:
            return False

        return self.helper(left_subtree.left, right_subtree.right) and self.helper(
            left_subtree.right, right_subtree.left
        )


ex1 = TreeNode(1)
ex1.left = TreeNode(2)
ex1.right = TreeNode(2)
ex1.left.left = TreeNode(3)
ex1.left.right = TreeNode(4)
ex1.right.left = TreeNode(4)
ex1.right.right = TreeNode(3)

ex2 = TreeNode(1)
ex2.left = TreeNode(2)
ex2.right = TreeNode(2)
ex2.left.right = TreeNode(3)
ex2.right.right = TreeNode(3)

iterative_solution = IterativeSolution()
recursive_solution = RecursiveSolution()

print(
    f"Example 1:\nInput: root = [1, 2, 2, 3, 4, 4, 3]\nOutput: {iterative_solution.isSymmetric(ex1)}\n",
    f"Example 1:\nInput: root = [1, 2, 2, 3, 4, 4, 3]\nOutput: {recursive_solution.isSymmetric(ex1)}\n",
)
print(
    f"Example 2:\nInput: root = [1,2,2,null,3,null,3]\nOutput: {iterative_solution.isSymmetric(ex2)}\n",
    f"Example 2:\nInput: root = [1,2,2,null,3,null,3]\nOutput: {recursive_solution.isSymmetric(ex2)}\n",
)
