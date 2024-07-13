from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next

            else:
                node = node.next

        return head

    # Time: O(n)
    # Space: O(1)


def traverse_linked_list(head: Optional[ListNode]) -> str:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return " -> ".join(map(str, result))


ex_1 = ListNode(1)
ex_1.next = ListNode(1)
ex_1.next.next = ListNode(2)

ex_2 = ListNode(1)
ex_2.next = ListNode(1)
ex_2.next.next = ListNode(2)
ex_2.next.next.next = ListNode(3)
ex_2.next.next.next.next = ListNode(3)

driver = Solution()

print(
    f"Example 1:\nInput: head = [1,1,2]\nOutput: {traverse_linked_list(driver.deleteDuplicates(ex_1))}\n"
)
print(
    f"Example 2:\nInput: head = head = [1,1,2,3,3]\nOutput: {traverse_linked_list(driver.deleteDuplicates(ex_2))}\n"
)
