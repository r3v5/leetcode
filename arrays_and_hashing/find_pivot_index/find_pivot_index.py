from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for num in nums:
            right_sum = total_sum - left_sum - num

            if right_sum == left_sum:
                return nums.index(num)

            left_sum += num

        return -1

    # Time Complexity: O(n)
