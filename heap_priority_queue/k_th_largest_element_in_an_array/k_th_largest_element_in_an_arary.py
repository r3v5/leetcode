import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create Max heap
        max_heap = [-1 * num for num in nums]
        heapq.heapify(max_heap)
        result = float("inf")

        while k > 0:
            result = -1 * heapq.heappop(max_heap)
            k -= 1

        return result


ex1 = [3, 2, 1, 5, 6, 4]
k_ex1 = 2

ex2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k_ex2 = 4

driver = Solution()

print(
    f"Example 1:\nInput: nums = [3,2,1,5,6,4], k = 2\nOutput: {driver.findKthLargest(ex1, k_ex1)}\n"
)
print(
    f"Example 2:\nInput: nums = [3,2,3,1,2,4,5,5,6], k = 4\nOutput: {driver.findKthLargest(ex2, k_ex2)}\n"
)
