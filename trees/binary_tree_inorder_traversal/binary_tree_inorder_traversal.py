from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # dfs in-order: left -> parent -> right
        if not root:
            return None

        result = []
        stack = []
        cur = root

        while stack or cur:

            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        return result


ex1 = TreeNode(1)
ex1.right = TreeNode(2)
ex1.right.left = TreeNode(3)

driver = Solution()

print(
    f"Example 1:\nInput: root = [1,null,2,3]\nOutput: {driver.inorderTraversal(ex1)}\n"
)
