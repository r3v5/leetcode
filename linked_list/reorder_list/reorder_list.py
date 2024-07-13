from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the mid
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half of linked list
        second = slow.next
        prev = None
        slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # reordering
        first = head
        second = prev

        while second:
            tmp_1 = first.next
            tmp_2 = second.next
            first.next = second
            second.next = tmp_1
            first = tmp_1
            second = tmp_2

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
ex_1.next = ListNode(2)
ex_1.next.next = ListNode(3)
ex_1.next.next.next = ListNode(4)

ex_2 = ListNode(1)
ex_2.next = ListNode(2)
ex_2.next.next = ListNode(3)
ex_2.next.next.next = ListNode(4)
ex_2.next.next.next.next = ListNode(5)

driver = Solution()

print(
    f"Example 1:\nInput: head = [1,2,3,4]\nOutput: {traverse_linked_list(driver.reorderList(ex_1))}\n"
)
print(
    f"Example 2:\nInput: head = [1,2,3,4,5]\nOutput: {traverse_linked_list(driver.reorderList(ex_2))}\n"
)
