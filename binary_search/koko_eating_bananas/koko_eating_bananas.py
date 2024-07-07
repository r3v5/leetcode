import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # possible k bananas per hour from one pile
        # [1...max(piles)]
        # ex. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # .     l                               r

        l = 1
        r = max(piles)
        k = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)

            if hours <= h:
                k = min(k, mid)
                r = mid - 1

            else:
                l = mid + 1

        return k


ex1 = [3, 6, 7, 11]
ex1_h = 8

ex2 = [30, 11, 23, 4, 20]
ex2_h = 5

ex3 = [30, 11, 23, 4, 20]
ex3_h = 6

driver = Solution()
print(
    f"Example 1:\nInput: piles = [3,6,7,11], h = 8\nOutput: {driver.minEatingSpeed(ex1, ex1_h)}\n"
)
print(
    f"Example 2:\nInput: piles = [30,11,23,4,20], h = 5\nOutput: {driver.minEatingSpeed(ex2, ex2_h)}\n"
)
print(
    f"Example 3:\nInput: piles = [30,11,23,4,20], h = 6\nOutput: {driver.minEatingSpeed(ex3, ex3_h)}\n"
)
