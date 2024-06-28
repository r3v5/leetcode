from collections import deque
from typing import List, Optional


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

    def find_min_node_in_bst(self, root: Optional["TreeNode"]) -> Optional["TreeNode"]:
        if not root:
            return None

        cur = root
        while cur.left:
            cur = cur.left

        return cur.val

    def find_max_node_in_bst(self, root: Optional["TreeNode"]) -> Optional["TreeNode"]:
        if not root:
            return None

        cur = root
        while cur.right:
            cur = cur.right

        return cur.val

    def insert_node_into_bst(
        self, root: Optional["TreeNode"], val: int
    ) -> Optional["TreeNode"]:
        new_node = TreeNode(val)

        if not root:
            return new_node

        cur = root

        while cur:
            if cur.val < val:

                if not cur.right:
                    cur.right = new_node
                    break

                else:
                    cur = cur.right

            else:
                if not cur.left:
                    cur.left = new_node
                    break

                else:
                    cur = cur.left

        return root

    def delete_node_from_bst(
        self, root: Optional["TreeNode"], key: int
    ) -> Optional["TreeNode"]:
        # base case
        if not root:
            return root

        # finding the node to delete
        cur = root

        if key > cur.val:
            cur.right = self.delete_node_from_bst(cur.right, key)
        elif key < cur.val:
            cur.left = self.delete_node_from_bst(cur.left, key)
        else:

            # check if there is only one child
            if not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left

            # if there are two children -> find the min node from right subtree and change the min node with node to delete
            # after delete the the min node from right subtree because now it's a parent node instead of node to delete
            min_node = self.find_min_node_in_bst(cur.right)
            cur.val = min_node.val
            cur.right = self.delete_node_from_bst(cur.right, min_node.val)

        return cur

    def find_node_in_bst(self, root: Optional["TreeNode"], target: int) -> bool:
        if not root:
            return False

        cur = root
        while cur:
            if cur.val == target:
                print(f"{target} is found in BST")
                return True
            elif cur.val < target:
                cur = cur.right
            else:
                cur = cur.left

        print(f"{target} is not found in BST")
        return False

    def inorder_recursively(self, root: Optional["TreeNode"]) -> List[int]:
        if not root:
            return []

        left = []
        right = []

        if root.left:
            left = self.inorder_recursively(root.left)

        if root.right:
            right = self.inorder_recursively(root.right)

        return left + [root.val] + right

    def inorder_iteratively(self, root: Optional["TreeNode"]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        cur = root

        while stack or cur:

            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res

    def preorder_recursively(self, root: Optional["TreeNode"]) -> List[int]:
        if not root:
            return []

        left = []
        right = []

        if root.left:
            left = self.preorder_recursively(root.left)

        if root.right:
            right = self.preorder_recursively(root.right)

        return [root.val] + left + right

    def preorder_iteratively(self, root: Optional["TreeNode"]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)

        return res

    def postorder_recursively(self, root: Optional["TreeNode"]) -> List[int]:
        if not root:
            return []

        left = []
        right = []

        if root.left:
            left = self.postorder_recursively(root.left)

        if root.right:
            right = self.postorder_recursively(root.right)

        return left + right + [root.val]

    def postorder_iteratively(self, root: Optional["TreeNode"]) -> List[int]:
        stack = [[root, False]]
        res = []

        while stack:
            cur, visited = stack.pop()

            if cur:

                if visited:
                    res.append(cur.val)

                else:
                    stack.append([cur, True])

                    if cur.right:
                        stack.append([cur.right, False])

                    if cur.left:
                        stack.append([cur.left, False])

        return res

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


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(11)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(5)


print(f"In-order traversal recursively: {root.inorder_recursively(root)}")
print(f"In-order traversal iteratively: {root.inorder_recursively(root)}\n")
print(f"Pre-order traversal recursively: {root.preorder_recursively(root)}")
print(f"Pre-order traversal iteratively: {root.preorder_iteratively(root)}\n")
print(f"Post-order traversal recursively: {root.postorder_recursively(root)}")
print(f"Post-order traversal iteratively: {root.postorder_iteratively(root)}\n")
print(f"BFS level order traversal: {root.bfs(root)}\n")


root = TreeNode(4)
root = root.insert_node_into_bst(root, 2)
root = root.insert_node_into_bst(root, 7)
root = root.insert_node_into_bst(root, 1)
root = root.insert_node_into_bst(root, 3)
root.find_node_in_bst(root, 7)
root = root.delete_node_from_bst(root, 7)
root.find_node_in_bst(root, 7)
print(f"Min node in BST: {root.find_min_node_in_bst(root)}")
print(f"Max node in BST: {root.find_max_node_in_bst(root)}")


preorder = [3, 9, 20, 15, 7]
index = 1
print(preorder[1 : index + 1])
