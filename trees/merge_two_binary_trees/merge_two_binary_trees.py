from collections import deque
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
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        # base case
        if not root1 and not root2:
            return None

        elif not root1:
            return root2

        elif not root2:
            return root1

        merged_root = TreeNode(root1.val + root2.val)
        queue = deque([[root1, root2, merged_root]])

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node1, node2, merged_node = queue.popleft()

                # process the left children
                if node1:
                    left1 = node1.left
                    right1 = node1.right
                else:
                    left1 = None
                    right1 = None

                if node2:
                    left2 = node2.left
                    right2 = node2.right
                else:
                    left2 = None
                    right2 = None

                if left1 or left2:

                    if left1 and left2:
                        merged_node.left = TreeNode(left1.val + left2.val)
                        queue.append([left1, left2, merged_node.left])

                    elif left1:
                        merged_node.left = TreeNode(left1.val)
                        queue.append([left1, None, merged_node.left])

                    elif left2:
                        merged_node.left = TreeNode(left2.val)
                        queue.append([None, left2, merged_node.left])

                if right1 or right2:

                    if right1 and right2:
                        merged_node.right = TreeNode(right1.val + right2.val)
                        queue.append([right1, right2, merged_node.right])

                    elif right1:
                        merged_node.right = TreeNode(right1.val)
                        queue.append([right1, None, merged_node.right])

                    elif right2:
                        merged_node.right = TreeNode(right2.val)
                        queue.append([None, right2, merged_node.right])

        return merged_root


ex1_root1 = TreeNode(1)
ex1_root1.left = TreeNode(3)
ex1_root1.right = TreeNode(2)
ex1_root1.left.left = TreeNode(5)
ex1_root2 = TreeNode(2)
ex1_root2.left = TreeNode(1)
ex1_root2.right = TreeNode(3)
ex1_root2.left.right = TreeNode(4)
ex1_root2.right.right = TreeNode(7)
driver = Solution()

print(
    f"Example 1:\nInput: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]\nOutput: {driver.mergeTrees(ex1_root1, ex1_root2)}"
)
