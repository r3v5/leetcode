from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-inf")
        l = 0

        for r in range(len(prices)):
            cur_profit = prices[r] - prices[l]

            if cur_profit < 0:
                l = r

            max_profit = max(max_profit, cur_profit)

        return max_profit


ex1 = [7, 1, 5, 3, 6, 4]
ex2 = [7, 6, 4, 3, 1]

driver = Solution()

print(f"Example 1:\nInput: prices = {ex1}\nOutput: {driver.maxProfit(ex1)}\n")
print(f"Example 2:\nInput: prices = {ex2}\nOutput: {driver.maxProfit(ex2)}\n")
