from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Use Bottom up DP Tabulation

        # base cases
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # dp[i] = max(rob, not rob)
            # rob = cur house profit + 2 houses before profit
            # not rob = keeping last profit
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

    # Time: O(n)
    # Space: O(n)
