from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # sort coins
        coins.sort()

        dp = [0] * (amount + 1)

        # 0 is base case
        for i in range(1, amount + 1):
            min_coins = float("inf")

            for coin in coins:
                diff = i - coin

                if diff < 0:
                    break

                min_coins = min(min_coins, dp[diff] + 1)

            dp[i] = min_coins

        if dp[amount] < float("inf"):
            return dp[amount]

        else:
            return -1

    # Time: O(coins * amount)
    # Space: O(amount)
