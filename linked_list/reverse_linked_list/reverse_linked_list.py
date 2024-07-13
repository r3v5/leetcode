from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traverse_linked_list(self, head: Optional["ListNode"]) -> List[int]:
        node = head
        result = []

        while node:
            result.append(node.val)
            node = node.next

        return result


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head

        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev

    # Time Complexity: O(n)
    # Space Complexity: O(1)


ex_1 = ListNode(1)
ex_1.next = ListNode(2)
ex_1.next.next = ListNode(3)
ex_1.next.next.next = ListNode(4)
ex_1.next.next.next.next = ListNode(5)

ex_2 = ListNode(1)
ex_2.next = ListNode(2)

driver = Solution()

print(
    f"Example 1:\nInput: head = [1,2,3,4,5]\nOutput: {ListNode().traverse_linked_list(driver.reverseList(ex_1))}\n"
)
print(
    f"Example 2:\nInput: head = [1,2]\nOutput: {ListNode().traverse_linked_list(driver.reverseList(ex_2))}\n"
)
