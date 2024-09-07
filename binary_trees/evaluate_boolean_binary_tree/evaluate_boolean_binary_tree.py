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
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # run dfs post-order traversal because firstly we want to get leaf nodes
        # use hashmap for mapping nodes and values
        hashmap = {}
        stack = [[root, False]]

        while stack:
            node, visited = stack.pop()

            if visited:

                # check if we reach leaf node
                if not node.left and not node.right:
                    hashmap[node] = node.val

                else:
                    # check if children are in hashmap
                    if node.left in hashmap and node.right in hashmap:

                        # apply OR operation
                        if node.val == 2:
                            hashmap[node] = hashmap[node.left] or hashmap[node.right]

                        # apply AND operation
                        if node.val == 3:
                            hashmap[node] = hashmap[node.left] and hashmap[node.right]

            else:
                stack.append([node, True])

                if node.right:
                    stack.append([node.right, False])

                if node.left:
                    stack.append([node.left, False])

        return hashmap[root]


ex1 = TreeNode(2)
ex1.left = TreeNode(1)
ex1.right = TreeNode(3)
ex1.right.left = TreeNode(0)
ex1.right.right = TreeNode(1)

ex2 = TreeNode(0)

driver = Solution()

print(
    f"Example 1:\nInput: root = [2,1,3,null,null,0,1]\nOutput: {driver.evaluateTree(ex1)}\n"
)
print(f"Example 2:\nInput: root = [0]\nOutput: {driver.evaluateTree(ex2)}\n")
