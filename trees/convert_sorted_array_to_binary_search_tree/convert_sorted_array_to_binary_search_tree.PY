from collections import deque
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

    def bfs(self, root: Optional["TreeNode"]) -> List[int]:
        if not root:
            return None

        result = []
        queue = deque([root])

        while queue:
            cur = queue.popleft()
            result.append(cur.val)

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)

        return result


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root


nums = [-10, -3, 0, 5, 9]
driver = Solution()
tree = driver.sortedArrayToBST(nums)
print(f"Output: {tree.bfs(tree)}")
