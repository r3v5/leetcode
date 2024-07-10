from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        # start with day 2 and go through each pair of prices to calculate profit
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]

            # find profitable day
            if profit > 0:
                total_profit += profit

        return total_profit


ex_1 = [7, 1, 5, 3, 6, 4]
ex_2 = [1, 2, 3, 4, 5]
ex_3 = [7, 6, 4, 3, 1]

driver = Solution()
print(f"Example 1:\nInput: prices = {ex_1}\nOutput: {driver.maxProfit(ex_1)}\n")
print(f"Example 2:\nInput: prices = {ex_2}\nOutput: {driver.maxProfit(ex_2)}\n")
print(f"Example 3:\nInput: prices = {ex_3}\nOutput: {driver.maxProfit(ex_3)}\n")
