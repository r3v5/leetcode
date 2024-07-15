from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # run dfs pre-order
        stack = [[[], 0]]
        result = []

        while stack:
            combination, length = stack.pop()

            # base case
            if length == len(nums):
                result.append(combination)

            for i in range(len(nums)):
                if nums[i] not in combination:
                    new_combination = combination + [nums[i]]
                    stack.append([new_combination, length + 1])

        return result

    # Time: O(n!)
    # Space: O(n)


ex_1 = [1, 2, 3]
ex_2 = [0, 1]
ex_3 = [1]

driver = Solution()
print(f"Example 1:\nInput: nums = {ex_1}\nOutput: {driver.permute(ex_1)}\n")
print(f"Example 2:\nInput: nums = {ex_2}\nOutput: {driver.permute(ex_2)}\n")
print(f"Example 3:\nInput: nums = {ex_3}\nOutput: {driver.permute(ex_3)}\n")
