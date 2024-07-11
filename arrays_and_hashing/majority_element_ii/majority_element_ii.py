from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        result = []

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        for num, freq in hashmap.items():
            if freq > len(nums) / 3:
                result.append(num)

        return result


# Time Complexity: O(n)
