from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # define the frequency array that is more that the length of nums
        # because we need [0] [1] [2] [3] [4] [5] [6]
        # numbers are indexed by their frequency

        freq = [[] for i in range(len(nums) + 1)]
        result = []
        counter = {}

        # count the amount of each integer
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)

        # iterate through the hashmap and add integers to freq array by index that is the frequency
        for n, c in counter.items():
            freq[c].append(n)

        for cell in range(len(freq) - 1, -1, -1):
            for num in freq[cell]:
                result.append(num)

                if len(result) == k:
                    return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
driver = Solution()
print(
    f"Example 1:\nInput: nums = {nums}, k = {k}\nOutput: {driver.topKFrequent(nums, k)}"
)
