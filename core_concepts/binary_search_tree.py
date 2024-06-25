from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        value: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def insert(self, data: int) -> None:
        # Check if the tree node is empty
        if self.value == None:
            self.value = data
            self.left = TreeNode()
            self.right = TreeNode()

        elif self.value == data:
            return

        elif data < self.value:
            if self.left == None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)

        elif data > self.value:
            if self.right == None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    def find(self, target: int) -> bool:
        if self.value == None:
            print(f"{target} is not found")
            return False

        stack = [self]

        while stack:
            cur = stack.pop()

            if cur.value == target:
                print(f"{target} is found")
                return True

            if cur.left and target < cur.value:
                stack.append(cur.left)

            if cur.right and target > cur.value:
                stack.append(cur.right)

        print(f"{target} is not found")
        return False

    def inorder_recursively(self) -> List[int]:
        if self.value == None and self.left == None and self.right == None:
            # If the tree is empty, return an empty list
            return []
        else:
            left = []
            right = []

            if self.left:
                left = self.left.inorder()

            if self.right:
                right = self.right.inorder()

            return left + [self.value] + right

    def inorder_iteratively(self) -> List[int]:
        res = []
        stack = []
        cur = self

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.value)
            cur = cur.right

        return res

    def preorder_iteratively(self) -> List[int]:
        if self.value is None:
            return []

        result = []
        stack = [self]

        while stack:
            cur = stack.pop()
            result.append(cur.value)

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)

        return result

    def postorder_iteratively(self) -> List[int]:
        if self.value is None:
            return []

        result = []
        stack = []
        cur = self
        last_visited = None

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                peek_node = stack[-1]
                if peek_node.right and peek_node.right != last_visited:
                    cur = peek_node.right
                else:
                    last_visited = stack.pop()
                    result.append(last_visited.value)

        return result


# Example usage
t = TreeNode(15)
t.insert(10)
t.insert(18)
t.insert(4)
t.insert(11)
t.insert(16)
t.insert(20)

print(t.postorder_iteratively())


class Solution:
    def maxDepthInorder(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = []
        cur = root
        res = 0
        depth = 0

        while stack or cur:
            while cur:
                stack.append((cur, depth + 1))
                cur = cur.left

            cur, depth = stack.pop()
            res = max(res, depth)

            cur = cur.right

        return res


class Solution:
    def maxDepthPostorder(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = []
        cur = root
        res = 0
        last_visited = None
        depth_stack = []

        while stack or cur:
            while cur:
                stack.append(cur)
                depth_stack.append(len(stack))
                cur = cur.left

            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                cur = peek.right
            else:
                last_visited = stack.pop()
                res = max(res, depth_stack.pop())

        return res
