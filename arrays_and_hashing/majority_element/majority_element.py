from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        for num, freq in hashmap.items():
            if freq > (n / 2):
                return num


ex1 = [3, 2, 3]
ex2 = [2, 2, 1, 1, 1, 2, 2]

driver = Solution()

print(f"Example 1:\nInput: nums = {ex1}\nOutput: {driver.majorityElement(ex1)}\n")
print(f"Example 2:\nInput: nums = {ex2}\nOutput: {driver.majorityElement(ex2)}\n")
