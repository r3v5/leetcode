from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def bfs(self, root: Optional["TreeNode"]) -> List[int]:
        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None

        # run bfs level order traversal
        queue = deque([root])

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                tmp = node.left
                node.left = node.right
                node.right = tmp

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root


ex1 = TreeNode(4)
ex1.left = TreeNode(2)
ex1.right = TreeNode(7)
ex1.left.left = TreeNode(1)
ex1.left.right = TreeNode(3)
ex1.right.left = TreeNode(6)
ex1.right.right = TreeNode(9)

driver = Solution()
new_root = driver.invertTree(ex1)
print(f"Example 1:\nInput: root = [4,2,7,1,3,6,9]\nOutput: {new_root.bfs(new_root)}\n")
