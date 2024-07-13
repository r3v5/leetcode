from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. find the middle
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # 3. use two pointers with left going from the begining and right going from the end of reversed second half
        # and check if the values aren't equal
        l = head
        r = prev
        while r:
            if l.val != r.val:
                return False

            l = l.next
            r = r.next

        return True

    # Time: O(n)
    # Space: O(1)


ex_1 = ListNode(1)
ex_1.next = ListNode(2)
ex_1.next.next = ListNode(2)
ex_1.next.next.next = ListNode(1)

ex_2 = ListNode(1)
ex_2.next = ListNode(2)


driver = Solution()
print(f"Example 1:\nInput: head = [1,2,2,1]\nOutput: {driver.isPalindrome(ex_1)}\n")
print(f"Example 2:\nInput: head = [1,2]\nOutput: {driver.isPalindrome(ex_2)}\n")
