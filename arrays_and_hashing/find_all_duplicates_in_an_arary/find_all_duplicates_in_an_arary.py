from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        result = []

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        for num, freq in hashmap.items():
            if freq == 2:
                result.append(num)

        return result

    # Time Complexity: O(n)


ex_1 = [4, 3, 2, 7, 8, 2, 3, 1]
ex_2 = [1, 1, 2]
ex_3 = [1]

driver = Solution()
print(f"Example 1:\nInput: nums = {ex_1}\nOutput: {driver.findDuplicates(ex_1)}\n")
print(f"Example 2:\nInput: nums = {ex_2}\nOutput: {driver.findDuplicates(ex_2)}\n")
print(f"Example 3:\nInput: nums = {ex_3}\nOutput: {driver.findDuplicates(ex_3)}\n")
