from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use Floyd's algorithm setting slow and fast pointers
        slow = nums[0]
        fast = nums[0]

        # prove that cycle exists (intersaction of slow and fast pointers)
        while True:

            # fast is 2x speed
            fast = nums[nums[fast]]

            # slow is 1x speed
            slow = nums[slow]

            if fast == slow:
                break

        # find where the cycle is by resetting fast and slow to 1x speed
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return slow

    # Time: O(n)
    # Space: O(1)


ex_1 = [1, 3, 4, 2, 2]
ex_2 = [3, 1, 3, 4, 2]
ex_3 = [3, 3, 3, 3, 3]

driver = Solution()
print(f"Example 1:\nInput: nums = [1,3,4,2,2]\nOutput: {driver.findDuplicate(ex_1)}\n")
print(f"Example 2:\nInput: nums = [3,1,3,4,2]\nOutput: {driver.findDuplicate(ex_2)}\n")
print(f"Example 3:\nInput: nums = [3,3,3,3,3]\nOutput: {driver.findDuplicate(ex_3)}\n")
