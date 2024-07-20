import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # base case
        if not stones:
            return 0

        # create max heap based on min heap making all values be negative
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # convert to positive numbers
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)

            if first > second:
                # add negative number since we have max heap and negative will be on top
                heapq.heappush(stones, -1 * (first - second))

            elif first == second:
                continue

        if len(stones) == 1:
            return -1 * stones[0]

        else:
            return 0

    # Time: O(nlogn)
    # Space: O(1)


stones = [2, 7, 4, 1, 8, 1]
driver = Solution()
print(
    f"Example 1:\nInput: stones = [2,7,4,1,8,1]\nOutput: {driver.lastStoneWeight(stones)}\n"
)
