from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            max_jump = nums[i]

            if i + max_jump >= target:
                target = i

        if target == 0:
            return True

        else:
            return False

    # Time: O(n)
    # Space: O(1)
