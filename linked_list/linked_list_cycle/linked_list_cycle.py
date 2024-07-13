from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False

    # Time: O(n)
    # Space: O(1)


ex_1 = ListNode(3)
ex_1.next = ListNode(2)
ex_1.next.next = ListNode(0)
ex_1.next.next.next = ListNode(-4)
ex_1.next.next.next.next = ex_1.next

driver = Solution()

print(f"Example 1:\nInput: [3,2,0,-4], pos = 1\nOutput: {driver.hasCycle(ex_1)}\n")
