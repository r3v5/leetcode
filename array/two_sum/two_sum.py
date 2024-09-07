from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap for storing numbers
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[n] = i


driver = Solution()
print(driver.twoSum([2, 7, 11, 15], 9))
print(driver.twoSum([3, 2, 4], 6))
print(driver.twoSum([3, 3], 6))
