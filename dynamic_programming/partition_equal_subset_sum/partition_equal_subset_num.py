from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # base case
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        dp = {0}

        for num in nums:
            new_sums = []

            for s in dp:
                new_sum = s + num

                if new_sum == target:
                    return True

                if new_sum < target:
                    new_sums.append(new_sum)

            dp.update(new_sums)

        return False

    # Time: O(n * sum(nums))
    # Space: O(n * sum(nums))
