from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        # move fast n times to find the link of node to delete
        while fast and n > 0:
            fast = fast.next
            n -= 1

        # move fast and slow pointers
        while fast:
            slow = slow.next
            fast = fast.next

        # delete nth node from the end
        slow.next = slow.next.next

        return dummy.next

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
ex_1.next.next.next.next = ListNode(5)
ex_1_n = 2

driver = Solution()
print(
    f"Example 1:\nInput: head = [1,2,3,4,5], n = 2\nOutput: {traverse_linked_list(driver.removeNthFromEnd(ex_1, ex_1_n))}\n"
)
