import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        max_heap = []
        result = []

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        for num, freq in hashmap.items():
            max_heap.append([-1 * freq, num])

        heapq.heapify(max_heap)

        while k > 0:
            # data = [freq, num]
            data = heapq.heappop(max_heap)
            num = data[1]
            result.append(num)
            k -= 1

        return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
driver = Solution()
print(
    f"Example 1:\nInput: nums = {nums}, k = {k}\nOutput: {driver.topKFrequent(nums, k)}\n"
)
