from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Time: O(n)
    # Space: O(1)


ex_1 = ListNode(1)
ex_1.next = ListNode(2)
ex_1.next.next = ListNode(3)
ex_1.next.next.next = ListNode(4)
ex_1.next.next.next.next = ListNode(5)

ex_2 = ListNode(1)
ex_2.next = ListNode(2)
ex_2.next.next = ListNode(3)
ex_2.next.next.next = ListNode(4)
ex_2.next.next.next.next = ListNode(5)
ex_2.next.next.next.next.next = ListNode(6)

driver = Solution()

print(f"Example 1:\nInput: head = [1,2,3,4,5]\nOutput: {driver.middleNode(ex_1).val}\n")
print(
    f"Example 2:\nInput: head = [1,2,3,4,5,6]\nOutput: {driver.middleNode(ex_2).val}\n"
)
