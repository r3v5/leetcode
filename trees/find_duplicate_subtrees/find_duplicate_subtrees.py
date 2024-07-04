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


# Time Complexity: BigO(n)
class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        if not root:
            return []

        # run dfs pre-order
        hashmap = {}
        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            # serialize each subtree to store the pattern in hashmap
            serialized_tree = self.serialize(node)

            if serialized_tree in hashmap:
                hashmap[serialized_tree] += 1
            else:
                hashmap[serialized_tree] = 1

            if hashmap[serialized_tree] == 2:
                result.append(node)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result

    # Serialize subtrees to identify duplicates
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"

        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            if not node:
                result.append("#")

            else:
                result.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)

        return ",".join(result)


ex1 = TreeNode(1)
ex1.left = TreeNode(2)
ex1.right = TreeNode(3)
ex1.left.left = TreeNode(4)
ex1.right.left = TreeNode(2)
ex1.right.right = TreeNode(4)
ex1.right.left = TreeNode(2)
ex1.right.left.left = TreeNode(4)
driver = Solution()

print(
    f"Example 1:\nInput: root = [1,2,3,4,null,2,4,null,null,4]\nOutput: {driver.findDuplicateSubtrees(ex1)}"
)
