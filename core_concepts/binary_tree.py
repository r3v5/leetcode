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

        node = root
        while node.left:
            node = node.left

        return node.val

    def find_max_node_in_bst(self, root: Optional["TreeNode"]) -> Optional["TreeNode"]:
        if not root:
            return None

        node = root
        while node.right:
            node = node.right

        return node.val

    def insert_node_into_bst(
        self, root: Optional["TreeNode"], val: int
    ) -> Optional["TreeNode"]:
        new_node = TreeNode(val)

        if not root:
            return new_node

        node = root

        while node:
            if node.val < val:

                if not node.right:
                    node.right = new_node
                    break

                else:
                    node = node.right

            else:
                if not node.left:
                    node.left = new_node
                    break

                else:
                    node = node.left

        return root

    def delete_node_from_bst(
        self, root: Optional["TreeNode"], key: int
    ) -> Optional["TreeNode"]:
        # base case
        if not root:
            return root

        # finding the node to delete
        node = root

        if key > node.val:
            node.right = self.delete_node_from_bst(node.right, key)
        elif key < node.val:
            node.left = self.delete_node_from_bst(node.left, key)
        else:

            # check if there is only one child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # if there are two children -> find the min node from right subtree and change the min node with node to delete
            # after delete the the min node from right subtree because now it's a parent node instead of node to delete
            min_node = self.find_min_node_in_bst(node.right)
            node.val = min_node.val
            node.right = self.delete_node_from_bst(node.right, min_node.val)

        return node

    def find_node_in_bst(self, root: Optional["TreeNode"], target: int) -> bool:
        if not root:
            return False

        node = root
        while node:
            if node.val == target:
                print(f"{target} is found in BST")
                return True
            elif node.val < target:
                node = node.right
            else:
                node = node.left

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

        result = []
        stack = []
        node = root

        while stack or node:

            while node:
                stack.append(node.val)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result

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

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result

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
        result = []

        while stack:
            node, visited = stack.pop()

            if visited:
                result.append(node.val)

            else:
                stack.append([node, True])

                if node.right:
                    stack.append([node.right, False])

                if node.left:
                    stack.append([node.left, False])

        return result

    def bfs(self, root: Optional["TreeNode"]) -> List[int]:
        if not root:
            return None

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

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
