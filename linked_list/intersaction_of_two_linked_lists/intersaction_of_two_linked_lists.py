from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        l1 = headA
        l2 = headB

        while l1 != l2:
            if l1:
                l1 = l1.next

            else:
                l1 = headB

            if l2:
                l2 = l2.next

            else:
                l2 = headA

        return l1

    # Time: O(m + n)
    # Space: O(1)


def traverse_linked_list(head: Optional[ListNode]) -> str:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return " -> ".join(map(str, result))


# Create intersection node
intersection = ListNode(8)
intersection.next = ListNode(4)
intersection.next.next = ListNode(5)

# Example 1
ex_1_list_1 = ListNode(4)
ex_1_list_1.next = ListNode(1)
ex_1_list_1.next.next = intersection

ex_1_list_2 = ListNode(5)
ex_1_list_2.next = ListNode(6)
ex_1_list_2.next.next = ListNode(1)
ex_1_list_2.next.next.next = intersection

driver = Solution()
result = driver.getIntersectionNode(ex_1_list_1, ex_1_list_2)
result_val = result.val if result else None

print(
    f"Example 1:\nInput: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3\nOutput: {result_val}\n"
)
