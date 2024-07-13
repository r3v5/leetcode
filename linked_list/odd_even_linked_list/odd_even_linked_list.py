from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        odd_ptr = head
        even_ptr = head.next
        even_head = head.next
        node = head
        i = 1

        while node:

            # found odd node -> connect odd pointer
            if i > 2 and i % 2 != 0:
                odd_ptr.next = node
                odd_ptr = odd_ptr.next

            # found even node -> connect even pointer
            elif i > 2 and i % 2 == 0:
                even_ptr.next = node
                even_ptr = even_ptr.next

            node = node.next
            i += 1

        # point last even node to null
        even_ptr.next = None

        # connect last odd node to the head of even nodes
        odd_ptr.next = even_head

        return head

    # Time: O(n)
    # Space: O(1)


# Utility function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Utility function to print a linked list
def print_linked_list(node: Optional[ListNode]):
    if not node:
        print("[]")
        return

    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print("[" + ", ".join(result) + "]")


# Example input 1
ex_1 = create_linked_list([1, 2, 3, 4, 5])
# Example input 2
ex_2 = create_linked_list([2, 1, 3, 5, 6, 4, 7])

# Test the solution
solution = Solution()

print("Example 1:")
result_1 = solution.oddEvenList(ex_1)
print_linked_list(result_1)

print("Example 2:")
result_2 = solution.oddEvenList(ex_2)
print_linked_list(result_2)
