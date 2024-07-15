from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        stack = [[[], 0]]
        result = []
        nums.sort()

        while stack:
            subset, index = stack.pop()
            result.append(subset)

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                stack.append([subset + [nums[i]], i + 1])

        return result

    # Time: O(2 ** n)
    # Space: O(n)


ex_1 = [1, 2, 2]
driver = Solution()
print(f"Example 1:\nInput: nums = {ex_1}\nOutput: {driver.subsetsWithDup(ex_1)}\n")
