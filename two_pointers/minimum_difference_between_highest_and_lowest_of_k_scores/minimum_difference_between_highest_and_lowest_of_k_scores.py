from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_diff = float("inf")
        nums.sort()

        l = 0
        r = k - 1

        while r < len(nums):
            min_diff = min(min_diff, nums[r] - nums[l])
            l += 1
            r += 1

        return min_diff

    # Time Complexity: O(nlogn)
