from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num_1 = ""
        num_2 = ""

        # reverse l1
        prev = None
        node = l1
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        new_l1 = prev
        while new_l1:
            num_1 += str(new_l1.val)
            new_l1 = new_l1.next

        # reverse l2
        prev = None
        node = l2
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        new_l2 = prev
        while new_l2:
            num_2 += str(new_l2.val)
            new_l2 = new_l2.next

        total_sum = str(int(num_1) + int(num_2))

        dummy = ListNode()
        node = dummy

        for digit in total_sum[::-1]:
            node.next = ListNode(int(digit))
            node = node.next

        return dummy.next

    # Time: O(n + m)
    # Space: O(n + m)


def print_linked_list(node: Optional[ListNode]):
    if not node:
        print("[]")
        return

    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print("[" + ", ".join(result) + "]")


# Example 1
ex_1_l_1 = ListNode(2)
ex_1_l_1.next = ListNode(4)
ex_1_l_1.next.next = ListNode(3)
ex_1_l_2 = ListNode(5)
ex_1_l_2.next = ListNode(6)
ex_1_l_2.next.next = ListNode(4)

# Example 2
ex_2_l_1 = ListNode(0)
ex_2_l_2 = ListNode(0)

# Example 3
ex_3_l_1 = ListNode(9)
node = ex_3_l_1
for _ in range(6):
    node.next = ListNode(9)
    node = node.next

ex_3_l_2 = ListNode(9)
node = ex_3_l_2
for _ in range(3):
    node.next = ListNode(9)
    node = node.next

driver = Solution()
print("Example 1:")
print("Input: l1 = [2, 4, 3], l2 = [5, 6, 4]")
print("Output:", end=" ")
print_linked_list(driver.addTwoNumbers(ex_1_l_1, ex_1_l_2))

print("\nExample 2:")
print("Input: l1 = [0], l2 = [0]")
print("Output:", end=" ")
print_linked_list(driver.addTwoNumbers(ex_2_l_1, ex_2_l_2))

print("\nExample 3:")
print("Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]")
print("Output:", end=" ")
print_linked_list(driver.addTwoNumbers(ex_3_l_1, ex_3_l_2))
