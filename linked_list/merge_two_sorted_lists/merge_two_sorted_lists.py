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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next

            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        if list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next

        if list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next

        return dummy.next

    # Time Complexity: O(n)
    # Space Comlexity: O(1)


ex_1_list_1 = ListNode(1)
ex_1_list_1.next = ListNode(2)
ex_1_list_1.next.next = ListNode(4)
ex_1_list_2 = ListNode(1)
ex_1_list_2.next = ListNode(3)
ex_1_list_2.next.next = ListNode(4)

ex_2_list_1 = ListNode(1)
ex_2_list_1.next = ListNode(3)
ex_2_list_1.next.next = ListNode(4)
ex_2_list_1.next.next.next = ListNode(5)
ex_2_list_1.next.next.next.next = ListNode(6)
ex_2_list_2 = ListNode(2)
ex_2_list_2.next = ListNode(3)
ex_2_list_2.next.next = ListNode(3)
ex_2_list_2.next.next.next = ListNode(4)

driver = Solution()

print(
    f"Example 1:\nInput: list1 = [1,2,4], list2 = [1,3,4]\nOutput: {ListNode().traverse_linked_list(driver.mergeTwoLists(ex_1_list_1, ex_1_list_2))}\n"
)
print(
    f"Example 2:\nInput: list1 = [1,3,4,5,6], list2 = [2,3,3,4]\nOutput: {ListNode().traverse_linked_list(driver.mergeTwoLists(ex_2_list_1, ex_2_list_2))}\n"
)
