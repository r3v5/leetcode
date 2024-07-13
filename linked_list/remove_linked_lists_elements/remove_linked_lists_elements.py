from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head
        dummy = ListNode(0, head)
        prev = dummy

        while node:
            if node.val == val:
                prev.next = node.next

            else:
                prev = node

            node = node.next

        return dummy.next

    # Time: O(n)
    # Space: O(1)


def traverse_linked_list(head: Optional[ListNode]) -> str:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return " -> ".join(map(str, result))


# Example 1
ex_1 = ListNode(1)
ex_1.next = ListNode(2)
ex_1.next.next = ListNode(6)
ex_1.next.next.next = ListNode(3)
ex_1.next.next.next.next = ListNode(4)
ex_1.next.next.next.next.next = ListNode(5)
ex_1.next.next.next.next.next.next = ListNode(6)
ex_1_val = 6

# Example 2
ex_2 = ListNode(7)
ex_2.next = ListNode(7)
ex_2.next.next = ListNode(7)
ex_2.next.next.next = ListNode(7)
ex_2_val = 7

driver = Solution()

result_1 = driver.removeElements(ex_1, ex_1_val)
result_2 = driver.removeElements(ex_2, ex_2_val)

print(
    f"Example 1:\nInput: head = [1,2,6,3,4,5,6], val = 6\nOutput: {traverse_linked_list(result_1)}\n"
)
print(
    f"Example 2:\nInput: head = [7,7,7,7], val = 7\nOutput: {traverse_linked_list(result_2)}\n"
)
